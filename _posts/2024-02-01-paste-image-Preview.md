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
   % edit under "Text" mode
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

   `Text` works best when you have a combination of texts and eqns.

    `Display` and `inline` modes work best when you have multi-line equations to show.

   ```latex
   \begin{aligned}
   p_t&=p_{t-1}+\epsilon_t \\
   r_t&=p_t-p_{t-1}=\epsilon_t \sim \text{IID} (0, \sigma^2)
   \end{aligned}
   
   % change eqn color
   % \usepackage{xcolor} % for mathcolor
   \begin{aligned}
   \mathcolor{blue}{
   p_t&=p_{t-1}+\epsilon_t \\
   r_t&\equiv \Delta p_t = p_t-p_{t-1}=\epsilon_t \sim \text{IID} (0, \sigma^2) 
   }
   \end{aligned}
   ```

   

2. copy and paste in Preview.



**LaTexIt**

[LaTeXiT](https://www.chachatelier.fr/latexit/index.php) is an equation editor. You can type LaTex eqns and dray'n drop them into other applications.

Even if LaTeXiT simplifies the whole process of "latexizing" you do not lose control over the advanced uses of the LaTeX engine. You can still **select the LaTeX engine, include packages, change the preamble, use scripts**… 

- The LaTeX preamble required to generate an image (`\documentclass{...}, \usepackage{...}, ...`) is automatically added. However, you can tune this preamble, just above the main text field, by dragging the handle down. Then you can see it. 

  <img src="https://drive.google.com/thumbnail?id=1UufO08v2J4J-vp4LI7_B6ulDLRuXDIAy&sz=w1000" alt="LaTexIt" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

- You can also change this preamble in the `Preferences` of the application, so that the modifications are kept. 

  <img src="https://drive.google.com/thumbnail?id=1rpcxEJIPtMTg43qiZRcB1Ro1VsjbdaR_&sz=w1000" alt="preamble" style="display: block; margin-right: auto; margin-left: auto; zoom:60%;" />

The export format can be set in the preferences. PDF is usually the best choice, since it is a "vectorial" format : the image can be resized without loss of quality. You can also choose the font size and the font color used for image generation.

- Once dropped in another application, a (PDF) equation can still be reopened in LaTeXiT by a simple "Copy/Paste". The LaTeX source code and the parameters of generation have been saved.

The modes `Display`, `Inline` and `Text` match the three LaTeX modes with the same names; please look at a LaTeX documentation to know more about their meaning. 

The `Eqnarray` mode is a handy shortcut to make multi-lines equations. It automatically uses `\begin{eqnarray*}...\end{eqnarray*}` around the LaTeX code.





**Reference**: <https://www.geekytidbits.com/how-to-insert-image-on-pdf-with-apple-preview/>