# Guides

The source of SkyKings' guides.

## Contributing

Contributing to the guides is very easy. 

First, you must be logged into a GitHub account. If you do not have one, you can create one at https://github.com/signup.

Now, you have two choices.

### 1. Creating a New Guide

To create a guide, open the [guides directory](guides) and create a new file.

![image](https://user-images.githubusercontent.com/49261529/233871991-0410dfd0-4005-436a-9844-de90dcf9732c.png)

![image](https://user-images.githubusercontent.com/49261529/233872066-ce4e6762-84ed-4b3b-bbaf-d526bd4364c9.png)


Now, name the file you just created. This will be the path your guide will be shown on, as well as the file extension (`.md`). For example:
- `fishing.md` is hosted under https://skykings.net/guides/fishing.
- `security.md` is hosted under https://skykings.net/guides/security.

Avoid making it too long, or difficult to remember. It should be short and related to the topic of the guide. For example:
- :white_check_mark: `garden.md` on a guide on how the Garden works
- :x: `how-to-make-a-lot-of-money.md`: Too long and hard to remember
- :x: `money-making.md` on a guide about Mining: Too unrelated to the guide's topic

Now, you can start writing your guide. The first thing you will need is the guide's metadata, which tells the website what the guide is about.

Metadata is written in [YAML](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html). There's an example below of how to write it:

    ```yaml {metadata}
    title: Example Guide
    description: |
      Demonstrates how to make a guide, especially the metadata.
      Multiple lines are supported.
    category: Examples
    author: Your Name
    tags:  # For SEO, just add phrases that might be searched for on google, also remove this comment
      - example
      - tag 1
      - tag 2
    hidden: true
    ```

You can then write your guide. For a full example, [click here](guides/example.md).

Once you've written your guide (or have started writing it), you can make a pull request.

First, save your changes by committing them.

![image](https://user-images.githubusercontent.com/49261529/233875899-be87c133-c71f-4510-b284-aa2e2a24050a.png)

Then you can create a pull request:

![image](https://user-images.githubusercontent.com/49261529/233875969-65791ac3-77b1-49fe-a7ca-77afc6bbe3c0.png)

Now, go through the pull reqest description, write a short summary, and check the boxes. **You must check the box under 'Licensing' at the bottom.**

Once you've done that, click the "Create pull request button", or use the arrow next to it to switch it to a draft if your guide is not finished.

Your guide will now be reviewed by our guides team. Please watch your pull request for updates.

If you made your pull request as a draft, and need to continue working on it, you can view your fork of the repository by 
clicking your profile icon in the top right, and selecting "My Repositories". Your guide will be saved in the "Guides" repository.

If you'd like, you can also make your own image for your guide. 
Just upload the image with the same filename as your guide (e.g. `example.png` for `example.md`) to the [`images` directory](images).

If you want to add images in the guide itself, you can upload them to a directory under images (such as `images/example/npc.png` for a guide titled `example.md`) 
and reference them using that same path (in this case, `/images/example/npc.png`), or just paste the image into the file you're editing.

## 2. Editing a Guide

Editing a guide is even simpler. As you're reading a guide on our website, there will be an edit button in the bottom right. 
Clicking this edit button will bring you straight to GitHub, where you can edit the guide. Then, once you're done, you can use the same steps as above to submit a pull request.

## Syntax

Guides are written in Markdown, you can find a syntax overview at https://www.markdownguide.org/cheat-sheet/.

For an example guide, [click here](https://github.com/SkyKings-Guild/Guides/blob/main/guides/example.md?plain=1).
