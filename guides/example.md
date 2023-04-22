```yaml {metadata}
# Guide metadata is written in YAML
# Syntax reference: https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html

title: Example Guide
description: |
  Demonstrates how to make a guide, especially the metadata.
  Multiple lines are supported.
category: Examples
author: Your Name
tags:
  - example
  - tag 1
  - tag 2
hidden: true  # Only used for internal stuff, you can ignore this
# Close the codeblock, then you can write the guide content
```

Some things to note:

- The title and description defined above will automatically be pasted
  on top of this, so don't worry about including it.
- The category is the section headers you see at [the main guides page](https://skykings.net/guides),
  and tags are only used for SEO purposes.
- By submitting a pull request for a guide, you agree to license your
  guide under the
  [Creative Commons Attribution-ShareAlike 4.0 International License](
  https://creativecommons.org/licenses/by-sa/4.0/).

Guide content goes around here, keep in mind that you do not need a header for the title,
and further headers should be at least header 2 (##)

# Syntax demonstrations

# Header 1

## Header 2

### Header 3

#### This keeps going forever

##### and ever

###### and ever

*Italics*

**Bold**

***Bold Italics***

~~Strikethrough~~

__Underline__

`Inline code for commands and stuff`

- List item 1
- List item 2
- List item 3

<p></p>

| Header 1        | Header 2        | Header 3        |
|-----------------|-----------------|-----------------|
| This is a table | This is a table | This is a table |

[Link with anchor text](https://example.com)

A link: <https://example.com>

![Image with alt text](/images/skykings-banner.jpg)

![Image with alt text](/images/skykings-banner.jpg "Image with title")

This image is a link:

[![image](/images/skykings-banner.jpg)](https://example.com)

<p style="text-align: center">HTML is supported, style and all.</p>
