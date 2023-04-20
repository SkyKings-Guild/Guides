import json
import markdown
import os
import yaml


def parse(file):
    with open(file, 'r') as f:
        contents = f.read()
    metadata_lines = []
    consumed_lines = 0
    split = contents.splitlines()
    for line in split:
        consumed_lines += 1
        if line != '---':
            metadata_lines.append(line)
        else:
            break
    metadata = yaml.safe_load("\n".join(metadata_lines))
    remaining_file = split[consumed_lines:]
    return metadata, markdown.markdown("\n".join(remaining_file))


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
            print(f'WARNING: Invalid metadata: {filename} ({str(e)})')
            continue
        metadata['identifier'] = identifier
        guide_metadata.setdefault(metadata['category'], [])
        guide_metadata[metadata['category']].append(metadata)
        guides[identifier] = content

if not os.path.exists('build'):
    os.mkdir('build')

for guide, html in guides.items():
    with open(os.path.join('build', f'{guide}.html'), 'w') as f:
        f.write(html)

with open(os.path.join('build', 'metadata.json'), 'w') as f:
    json.dump(guide_metadata, f)

added_files = ['metadata.json'] + [f'{guide}.html' for guide in guides]

for file in scandir('build'):
    if file not in added_files:
        os.remove(os.path.join('build', file))
    

