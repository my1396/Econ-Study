---
layout: post
tag: misc
title: Paste Image Into pdf on MacOS Preview
---


It is possible to paste an image into a PDF page from the clipboard, but you must first convert the image to an “object image” first.

**Steps**

1. Open the source image file and target PDF using Preview
2. Press the following key sequences:

   - ⌘+A (select the entire image)
   - ⌘+C (copy it to the clipboard)
   - ⌘+V (paste the image on top of the original as an “object image”).
3. Click on the object image you just pasted on top of the original image
4. Press ⌘+C to copy the new object image to the clipboard
5. Click on to target page and press ⌘+V to paste the image into it.



**Paste LaTex eqns as images in pdf**

1. use LaTeXiT to edit eqns and export as PNG.

   ```latex
   \colorbox{white}{$y_t = \phi^k y_{t-k} + \sum_{j=0}^{k-1}\phi^j \varepsilon_{t-j}$}
   ```

   By default, LaTeXiT creates an image with transparent color.

   You can use `\colorbox{white}{...}` to create a white background for your text.

   If your text spans several lines, put your text inside a `minipage` such that the text got wrapped.

   ```latex
   \noindent
   \colorbox{white}{
   \begin{minipage}{\linewidth}
   $f(x)=\pi^2+(1-\pi)^2$, and $g(x)=2\pi(1-\pi)$\\
   Then $(\frac{1}{2}, \frac{1}{2})$ is the only point \\
   where $f(x)$ and $g(x)$ intersect.
   \end{minipage}
   }
   
   % if you don't want any background color
   % the following cmd do the work
   \noindent
   $f(x)=\pi^2+(1-\pi)^2$, and $g(x)=2\pi(1-\pi)$\\
   Then $(\frac{1}{2}, \frac{1}{2})$ is the only point \\
   where $f(x)$ and $g(x)$ intersect.
   
   % change text color
   \noindent\textcolor{blue}{
   $f(x)=\pi^2+(1-\pi)^2$, and $g(x)=2\pi(1-\pi)$\\
   Then $(\frac{1}{2}, \frac{1}{2})$ is the only point \\
   where $f(x)$ and $g(x)$ intersect.
   }
   ```

   

2. copy and paste in Preview.



**Reference**: <https://www.geekytidbits.com/how-to-insert-image-on-pdf-with-apple-preview/>