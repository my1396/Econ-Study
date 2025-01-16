---
layout: post
title: Insert Images Using Relative Links
tag: programming
update: 2024-01-20
---

### Relative Links

<https://github.blog/2016-12-05-relative-links-for-github-pages/>

**Embed files using relative path**

If you have a Markdown file in your repository at `docs/page.md`, and you want to link from that file to `docs/another-page.md`, you can do so with the following markup:

```scss
[a relative link](another-page.md)
```

When you view the source file on GitHub.com, the relative link will continue to work, as it has before, but now, when you publish that file using GitHub Pages, the link will be silently translated to `docs/another-page.html` to match the target page’s published URL.



**Embed images using <span style='color:#32CD32'>relative path</span>**

```html
<img src="{{site.baseurl}}/images/image-20230730113759915.png" alt="quadrant geometry" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />
```

- The drawback with this method is that it does not provide local preview in desktop apps, like Visual Studio or Typora.
- <span style='color:#32CD32'>Support preview using the local host `http://127.0.0.1:4000/`</span> though.
- The advantage is that it does not rely on any cloud services, such as Google Drive. The image folder is hosted on GitHub, meaning it won't have domin restrictions when travel abroad or it won't be affected by service updates from Google.

- `baseurl` is set in the `_config.yml`, it is the name of sub-directory the site is served from. E.g., for the following url `https://my1396.github.io/Econ-Study/2023/10/03/HTML.html`, 
- url is `https://my1396.github.io`; 
  
- baseurl is `/Econ-Study`; 
  
- page url is `/2023/10/03/HTML.html`.





### Upload Images as Assets

[Uploading assets](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#uploading-assets)

You can upload assets like images by dragging and dropping, selecting from a file browser, or pasting. You can upload assets to `issues`, `Pull requests`, comments, and `.md` files in your remote Github repository.


- When you drag and drop, the "Write" box will generate a link for the file.

- Click "Preview" to see if the image shows alright.

Using the following code to insert the image you uploaded:

```html
<img src="https://github.com/my1396/Econ-Study/assets/14339495/e84211f5-038e-41d3-bf78-40785de291d6" alt="IVT.svg" style="display: block; margin-right: auto; margin-left: auto; zoom:150%;" />
```

**Comments**: 

- It's <span style='color:#32CD32'>safer and faster to use project self-contained images</span>, for instance, in a folder `images` or `assets`. In this way, it doesn't depend on an external server like Google. 
- The probelm with Cloud Storage is that when Google updates their terms, your website is corrupted. You have to make changes to your source codes to meet the requirements of the new terms (see the follwing section for an instance).
- Self-contained images protect you from website corruption, which is more stable.
- It is fatest for your website to load images when the files are on GitHub. But then you need to upload lots of images. As GitHub won't process a large amount at one time, you need to split the upload into small batches.

___



### Link to Google Drive Images

<https://www.intodeeplearning.com/embedding-images-in-google-drive-to-markdown/>

Setting on Google Drive: Set **Restricted** mode of sharing to **Anyone with the link**.

For example:

- my link: `https://drive.google.com/file/d/1L07w0_Qg9q-0Ukm4-K3i8ffyk34FqTzA/view?usp=sharing`
- \<ID of image\> is after `d` and before `view?usp=sharing`, i.e., `1L07w0_Qg9q-0Ukm4-K3i8ffyk34FqTzA` in this case.
- my embeddinwg link: `https://drive.google.com/uc?id=1L07w0_Qg9q-0Ukm4-K3i8ffyk34FqTzA`

To embed an image using markdown, use the following:

```markdown
![Example Image](https://drive.google.com/uc?id=1bXzYeegauqB2M6-VZwitEeXHmMiYZIUY)
```
Markdown syntax to insert an image link: Start with an exclamation mark (`!`), followed by alt text in brackets, and the path or URL to the image asset in parentheses.


Add some style adjustment:

```html
<img src="https://drive.google.com/uc?id=1-CMHtcl4dcjjA9aWoqiThd2OCznm25rb" alt="image-20210520120254672" style="zoom:50%;" />

<img src="https://drive.google.com/uc?id=1bXzYeegauqB2M6-VZwitEeXHmMiYZIUY"
     alt="sample image"
     style="display: block; margin-right: auto; margin-left: auto; width: 90%;
     box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)" />
```

**Update** (Since Jan 2024):

- Errors show up as Google updates some settings: 

  > Failed to load resource: the server responded with a status of 403 ()

  See [Here](https://issuetracker.google.com/issues/319531488?pli=1) for a detailed problem description and discussion.

- Solution: replace the old code with the new one as follows.

  1. replace `uc?` with `thumbnail?`;
  2. add `&sz=w1000` after the image ID.

  ```html
  <img src="https://drive.google.com/uc?id=1-CMHtcl4dcjjA9aWoqiThd2OCznm25rb" alt="image-20210520120254672" style="zoom:50%;" />
  <img src="https://drive.google.com/thumbnail?id=1-CMHtcl4dcjjA9aWoqiThd2OCznm25rb&sz=w1000" alt="image-20210520120254672" style="zoom:50%;" />
  ```



  
