import json
import markdown2
import os
import re
import shutil
import yaml

image_regex = re.compile(r'!\[(.*?)]\(/images/(.*?)(?: \"(.+)\")?\)')

md_extras = [
    "cuddled-lists",
    "strike",
    "tables",
]


def replace_image(match):
    base = f'![{match.group(1)}](https://raw-guides.skykings.net/images/{match.group(2)}'
    if match.group(3) is None:
        return base + ')'
    return base + f' "{match.group(3)}")'


def parse(file):
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
    metadata_lines = []
    consumed_lines = 0
    split = contents.splitlines()
    for line in split:
        if consumed_lines == 0 and line != '```yaml {metadata}':
            return None, None
        consumed_lines += 1
        if consumed_lines == 1:
            continue
        if line == '```':
            break
        if line == '---':
            break
        metadata_lines.append(line)
    metadata_lines = metadata_lines
    # noinspection PyShadowingNames
    metadata = yaml.safe_load("\n".join(metadata_lines))
    remaining_file = "\n".join(split[consumed_lines:])
    remaining_file = image_regex.sub(replace_image, remaining_file)
    html = markdown2.markdown(remaining_file, extras=md_extras)
    # this is really weird but it works
    html = html.replace('<tbody>', '')
    html = html.replace('</thead>', '')
    html = html.replace('<thead>', '<tbody>')
    return metadata, html


def scandir(directory, *, odir=None):
    for entry in os.scandir(directory):
        if entry.is_dir():
            yield from scandir(entry.path, odir=odir or directory)
        else:
            path = os.sep.join(str(entry.path).split(os.sep)[1:])
            yield path


guide_metadata = {}

guides = {}

for filename in scandir('guides'):
    if filename.endswith('.md'):
        print(f'Building {filename}...')
        identifier = filename.split(os.sep)[-1][:-3]
        file = os.path.join('guides', filename)
        metadata, content = parse(file)
        if metadata is None:
            print(f'ERROR: Missing metadata: {file}')
            continue
        if metadata.get('hidden', False):
            guides[identifier] = content
            continue
        # validate metadata
        try:
            assert 'title' in metadata
            assert 'category' in metadata
            assert 'description' in metadata
            assert 'author' in metadata
        except AssertionError as e:
            print(f'ERROR: Invalid metadata: {filename} ({str(e)})')
            continue
        metadata['identifier'] = identifier
        guide_metadata.setdefault(metadata['category'], [])
        guide_metadata[metadata['category']].append(metadata)
        guides[identifier] = content

if not os.path.exists('build'):
    os.mkdir('build')

for guide, html in guides.items():
    with open(os.path.join('build', f'{guide}.html'), 'w', encoding='utf-8') as f:
        f.write(html)

with open(os.path.join('build', 'metadata.json'), 'w', encoding='utf-8') as f:
    json.dump(guide_metadata, f)

added_files = ['metadata.json'] + [f'{guide}.html' for guide in guides]

for file in scandir('build'):
    if file not in added_files:
        os.remove(os.path.join('build', file))
try:
    os.removedirs('build/images')
except FileNotFoundError:
    pass

shutil.copytree('images/', 'build/images', copy_function=shutil.copy)
shutil.copy('misc/robots.txt', 'build/robots.txt')
