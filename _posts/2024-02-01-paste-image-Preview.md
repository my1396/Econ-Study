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

   If you have a single line equation, you can use `\colorbox{white}{...}` to create a white background for your text.

   If your text **spans several lines**, put your text inside a `minipage` such that the text got wrapped.

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

   Colored `eqn + text`, use <span style='color:#32CD32'>`textcolor`</span> in `Text` mode.

   <img src="https://drive.google.com/thumbnail?id=17VEWrpFNIA1tICSP6JgupCHITg73hbkE&sz=w1000" alt="color_eqn" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

   Differnt environments:

   - `Text` works best when you have a combination of texts and eqns.

   - `Display` and `Inline` modes work best when you have only multi-line *equations* to show.

   For example, in `Display` mode:

   ```latex
   \begin{aligned}
   p_t&=p_{t-1}+\epsilon_t \\
   r_t&=p_t-p_{t-1}=\epsilon_t \sim \text{IID} (0, \sigma^2)
   \end{aligned}
   ```

   `textcolor` doesn't work inside `aligned` environment. Have to use <span style='color:#32CD32'>**`mathcolor`**</span> from the `xcolor` package.

   ```latex
   % change eqn color in `Display` mode
   % \usepackage{xcolor} % for mathcolor
   \begin{aligned}
   \mathcolor{blue}{
   p_t&=p_{t-1}+\epsilon_t \\
   r_t&\equiv \Delta p_t = p_t-p_{t-1}=\epsilon_t \sim \text{IID} (0, \sigma^2) 
   }
   \end{aligned}
   
   % add white background box in `Text` or `Display` modes
   \noindent
   \colorbox{white}{
   \begin{minipage}{\linewidth}
   $$
   \begin{aligned}
   \mathcolor{blue}{
   p_t&=p_{t-1}+\epsilon_t \\
   r_t&\equiv \Delta p_t = p_t-p_{t-1}=\epsilon_t \sim \text{IID} (0, \sigma^2) 
   }
   \end{aligned}
   $$
   \end{minipage}
   }
   ```

   <img src="https://drive.google.com/thumbnail?id=15ITke2nlWAdGBNhVccrNhQIejk4gW7SH&sz=w1000" alt="color_display" style="display: block; margin-right: auto; margin-left: auto; zoom:40%;" />

2. copy and paste in Preview.



**LaTexiT example**

```latex
\colorbox{white}{
\begin{minipage}{0.7\linewidth}
    \begin{align*}
    & \texttt{\textbackslash num\{0.123\}}   &  \quad  & \num{0.123} \\
    & \texttt{\textbackslash num\{0,1234\}}  &  \quad  & \num{0,1234} \\
    & \texttt{\textbackslash num\{.12345\}}  &  \quad  & \num{.12345} \\
    & \texttt{\textbackslash num\{3.45d-4\}} &  \quad  & \num{3.45d-4} \\ 
    & \texttt{\textbackslash num\{-e10\}}    &  \quad  & \num{-e10} 
\end{align*}
\end{minipage}
}
```

<img src="https://drive.google.com/thumbnail?id=1b071iEketT2y4EnbLom1T-1JYw4udrKm&sz=w1000" alt="align" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />



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



### LaTeXiT Tables

```latex
\usepackage{caption}
\DeclareCaptionFormat{mycaptionformat}{
  \colorbox{white}{\parbox{\dimexpr\textwidth-2\fboxsep\relax}{#1#2\color{black}\bfseries#3}}
} 
\captionsetup[table]{format=mycaptionformat,font={color=black,bf},skip=0pt}

\begin{document}

% table with white background
\begin{table}
\caption{my caption}
\colorbox{white}{
    \centering
    \begin{tabular}{@{}ll|ll|l@{}}
    &  \multicolumn{1}{c}{}   & \multicolumn{2}{c}{\textbf{sex}} &     \\ 
    &     & 0 (male)         & 1 (female)         & Sum \\
    \cline{2-5}
    \multirow{2}{*}{\textbf{arrhythmia}} & 0 (absence)    & 85         & 160        & 245 \\
    & 1 (presence)   & 117        & 89         & 206 \\
    \cline{2-5}
                                & Sum & 202        & 249        & 451 \\ 
    \end{tabular}}
\end{table}

\end{document}
```









### Adjust image size in Notes 

1. Right-click image. Select Open with Preview.
2. **Tools** in the menu $\rightarrow$ **Adjust Size**.
3. A menu should pop up allowing you to adjust the size. Make necessary changes and click Ok.
4. Select entire image (Cmd + A) and copy it to clipboard (Cmd + C).
5. Open notes and paste image (Cmd + V)



**Reference**: <https://www.geekytidbits.com/how-to-insert-image-on-pdf-with-apple-preview/>