// Add a Copy button to each fenced code block and handle clipboard copy
// Works for Rouge-generated markup like: <figure class="highlight"><pre><code>...</code></pre></figure>
(function () {
  function addCopyButtons() {
    // Prefer code blocks in figure.highlight; also handle plain pre > code
    const codeBlocks = document.querySelectorAll('figure.highlight, pre>code');
    if (!codeBlocks.length) return;

    codeBlocks.forEach(node => {
      let container, codeEl;

      if (node.matches('figure.highlight')) {
        container = node; // figure.highlight
        codeEl = container.querySelector('pre code');
      } else if (node.matches('pre>code')) {
        codeEl = node;
        container = node.closest('pre');
      }

      if (!container || !codeEl) return;

      // Avoid duplicate buttons
      if (container.querySelector('.copy-code-btn')) return;

      // Create button
      const btn = document.createElement('button');
      btn.className = 'copy-code-btn';
      btn.type = 'button';
      btn.title = 'Copy code';
      btn.setAttribute('aria-label', 'Copy code');
      btn.innerHTML = '<i class="codicon codicon-copy"></i>';

  // Position button and mark container for padding adjustment
  container.style.position = container.style.position || 'relative';
  container.classList.add('has-copy-btn');
      container.appendChild(btn);

      // Copy handler
      btn.addEventListener('click', async () => {
        const text = codeEl.innerText;
        try {
          await navigator.clipboard.writeText(text);
          btn.classList.add('copied');
          btn.innerHTML = '<i class="codicon codicon-check"></i>';
          setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="codicon codicon-copy"></i>';
          }, 1200);
        } catch (e) {
          // Fallback for older browsers
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); } catch (err) {}
          document.body.removeChild(ta);
          btn.classList.add('copied');
          btn.innerHTML = '<i class="codicon codicon-check"></i>';
          setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="codicon codicon-copy"></i>';
          }, 1200);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addCopyButtons);
  } else {
    addCopyButtons();
  }
})();
