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


guide_metadata = {}

guides = {}


for file in os.listdir('guides'):
    if file.endswith('.md'):
        identifier = file[:-3]
        file = os.path.join('guides', file)
        metadata, content = parse(file)
        # validate metadata
        assert 'title' in metadata
        assert 'category' in metadata
        assert 'description' in metadata
        assert 'author' in metadata
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

for file in os.listdir('build'):
    if file not in added_files:
        os.remove(os.path.join('build', file))
    

