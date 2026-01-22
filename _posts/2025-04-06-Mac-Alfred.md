---
layout: post
title: "Mac Software – Alfred"
tag: life
update: 2025-04-06
---

[Alfred](https://www.alfredapp.com) is a Mac Spotlight replacement app and enhancement, which boosts your efficiency with hotkeys, keywords, text expansion and more. It is a powerful launcher that helps you quickly find files, launch applications, and perform various tasks on your Mac.

--------------------------------------------------------------------------------

Q: Is Alfred free?  
A: Go to [Alfred homepage](https://www.alfredapp.com), scroll down to "Productivity at your Fingertips". The functions without stars are free to use. The starred functions require the paid "Alfred Powerpack" license.

What are in the free version?

- Find and launch applications, files (same as Mac Spotlight)
- Web Search

What are NOT in the free version but very useful, would be a big loss if missing it?

- Snippets (I use it all the time)
- Clipboard History
- Workflow

--------------------------------------------------------------------------------

**Useful resources:**

- [Help Page](https://www.alfredapp.com/help/features/) 
- [Nice Tutorial: My Alfred Setup](https://stefanzweifel.dev/posts/2021/02/03/my-alfred-setup/)


**Alfred Hotkeys** 

- <kbd>^</kbd> + <kbd>Space</kbd>: show Alfred bar
  
  Here I replace Mac Spotlight with Alfred. ^ + Space was was the default Spotlight shortcut. 
  To replace it with Alfred, go to System Settings > Keyboard > Keyboard Shortcuts > Spotlight, and uncheck the default shortcut. Then set Alfred hotkey to ^ + Space in Alfred Preferences > General > Alfred Hotkey.

- <kbd>⌘,</kbd> : preferences

- <kbd>␣f-name</kbd>: search internal files and folders with name `f-name`
    - <kbd>⌘</kbd> + <kbd>Enter</kbd>: show file location in folder

--------------------------------------------------------------------------------

## Setup

- Uncheck automatic update
- Hide/Show Alfred icon in menu bar
  
  Appearance > Options > **Check "Hide menu bar icon"**

  <img src="https://drive.google.com/thumbnail?id=1uFDLFa27a-Nrs2zfnYx-EGXuTASO1pjP&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />


--------------------------------------------------------------------------------

**Highlight Features:**

- **Web Search**: Efficient way to do customized searches. 
  
  A <span class="env-orange">drawback</span> is that it opens a new tab in the browser each time you search even though you have already got the tab open in your browser.
  
  How to use: Type `g <keyword>` to search on Google. Don’t need to open browser, navigate to Google, and start typing then. 
  
  My Custom Web Search Definitions:

  - `g <keyword>` to search on Google
  - `youdao <keyword>` to search on 有道词典
  - `ord <keyword>` to search on [Ordnett](https://www.ordnett.no) 挪威语词典

- **Code snippet**: keywords to be replaced by your snippets. Quick way to type phrases you use again and again. 
  
  Import snippet extensions: [↩](https://www.alfredapp.com/extras/snippets/)
  
  - [Emoji Pack](https://joelcalifa.com/blog/alfred-emoji-snippet-pack/) by Joel Califa
  
  Type `snip <keyword>` to look up snippets.

- **Dictionary**: type `define <word>` to find the definition of the word.

- **Terminal**: type `> your shell cmd …` to open terminal and run shell commands.





--------------------------------------------------------------------------------

## Alfred Snippets

Code snippet（begin with two colons `::`）
- `cs_green`: html colored span, green
- `cs_orange`: html colored span, orange

<figure style="text-align: center;">
  <img src="https://drive.google.com/thumbnail?id=1U10XBFzhE2_T14l81VoV7X17o4qtvlBf&sz=w1000" alt="Alfred Snippets" style="display: block; margin-right: auto; margin-left: auto; zoom:80%;" />
  <figcaption>Fig Source: @Brooke Kuhlmann, <a href="https://alchemists.io/articles/alfred_snippets">Alfred Snippets</a>.</figcaption>
</figure>

**Snippet setting**

- **Uncheck “Word based”**
  
  When the "Word based" is enabled, the snippet search sees the `:` as part of the word, and so searching “whiskey” would return no results. 

  Unchecking “Word based” makes it act more like a fuzzy search.

- When creating a new snippet, use the `prefix` option, e.g., `::`, so that you can batch change later. 
  
  <img src="https://drive.google.com/thumbnail?id=1hrZrj1QYoXHXWBbOYh73t3FRdOVrs-0C&sz=w1000" alt="New collection" style="display: block; margin-right: auto; margin-left: auto; margin-top: 2ex; zoom:100%;" />

  Optionally, you can use the `suffix` option too, e.g., `:<keyword>:`. The [emoji snippet pack](https://joelcalifa.com/blog/alfred-emoji-snippet-pack/) by Joel Califa uses this format.

  See [HERE](https://gist.github.com/rxaviers/7360908) for a list of emoji snippets frequently used. 

  The following table shows some emojis I use most often:

  | Emoji  | Snippet Keyword               |
  | -----  | ----------------------------- |
  | ☺️     | `:relaxed:` or `:smileshy:`   |
  | 😂     | `:joy:`                       |
  | 🙈     | `:see_no_evil:`               |
  | 🤣     | `:rofl:`                      |
  | 😆     | `:laughing:` or `:satisfied:` |
  | 🤩     | `:star_struck:`               |
  | 🤪     | `:zany_face:`                 |
  | 😎     | `:sunglasses:`                |
  | 🙏     | `:pray:` or `:thanks:`        |
  | ❤️     | `:heart:`                     |
  | 👍     | `:thumbs␣up:` or `:+1:`       |
  | 👏     | `:clap:`                      |
  | ✅     | `:checkmark:`                 |
  | ❌     | `:x:`                         |
  | 💡     | `:bulb:`                      |



- When you import snippets from other sources, you may want to **uncheck "Strip snippets of ‘auto expand’ flag."** 
  
  <img src="https://drive.google.com/thumbnail?id=1_c5GL_9DudwXGNfRNsoB2U-ULK0Sj55k&sz=w1000" alt="Snippets auto expansion" style="display: block; margin-right: auto; margin-left: auto; zoom:50%;" />

  This setting preserves all imported snippets if “Auto expansion allowed” is enabled.  
  Otherwise, you have to manually check it for each snippet. For large snippet packs, it’s a pain to click hundreds of times.

  The list of snippets contains one column `A→`; it means "Auto expansion allowed". Toggle it on/off for each snippet. It controls whether the snippet can be auto expanded when typing the prefix.

--------------------------------------------------------------------------------

Q: Snippet auto expand does not work in <span class="env-green">VS Code</span>?  
A: When you type the snippet keyword, the snippet is copied to clipboard, and you need to paste it (⌘V) to insert the snippet content.

How to insert Alfred snippet in VS Code. Two methods:

- Method 1: Type the snippet keyword, then press ⌘V to paste the snippet content.
- Method 2: This is useful especially when you cannot remember the exact snippet keyword.
  
  <ol type="pa">
    <li><kbd>⌃</kbd> + <kbd>Space</kbd> to launch Alfred.</li>
    <li>Type the snippet keyword, e.g., <code>snip smile</code>, a list of matching snippets appear.</li>
    <li>Choose the desired snippet using arrow keys, then press <kbd>Enter</kbd> to paste it into VS Code.</li>
  </ol>

--------------------------------------------------------------------------------

**Search Snippet Keyword Shortcut**: `snip` is the default keyword to do a fuzzy search of snippets.

You can change `snip` to `s` in Alfred Preferences > Features > Snippets > Snippet Keyword.

Issue: When I type `s␣`, Alfred pops up a System Settings window instead of snippet search results. The reason is that `s` invokes the macOS System Settings at the first on the result list. 

To fix this, follow the steps:

1. Type `s`, then choose the snippets search result using arrow keys or ⌘2, Alfred now waits for further input of snippet keyword.
2. Type the snippet keyword, e.g., `smile`, then the matching snippets appear.
3. Choose the desired snippet using arrow keys and hit Enter to paste it.



--------------------------------------------------------------------------------

## Clipboard History

Clipboard history Keyboard shortcit: ⌥⌘C

Issue: Alfred snippets pasting from clipboard rather than snippet.  
Fix: Slow down key events. I changed it from 0.5s to 0.6s. 


## Sync preferences between Macs

**Primary Mac**: the one you want to sync from. The settings on this Mac will overwrite anything you have on the second Mac.

1. Preferences > Advanced > Set preferences folder... > Choose the location where you want to sync your settings (e.g. `~/Dropbox/Alfred/`) and click `Set folder and restart Alfred`.
2. Set Alfred.alfredpreferences to [always be available offline](https://www.alfredapp.com/help/advanced/sync/#always-offline).

**Second Mac**

1.  Check that your newly added settings file is available. You should see an Alfred.alfredpreferences file in the folder you picked.
2.  [Set the file to be available offline](https://www.alfredapp.com/help/advanced/sync/#always-offline) and wait for the download to finish.
3.  Launch Alfred's preferences to the Advanced tab and click on `Set preferences folder...`
4.  Find the folder in which your first Mac's Alfred.alfredpreferences file is located and click `Set folder and restart Alfred`
5.  Once Alfred has restarted, you'll be using your synced settings.

ref: [Syncing Your Alfred Settings Between Macs](https://www.alfredapp.com/help/advanced/sync/)

--------------------------------------------------------------------------------

ref:

- <https://www.reddit.com/r/Alfred/comments/14rn8er/alfred_snippets_pasting_from_clipboard_rather/>
- <https://www.alfredapp.com/help/troubleshooting/snippets/#partial>





