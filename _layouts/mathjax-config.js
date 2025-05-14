// enable inline eqn and add new macro definitions
window.MathJax = {
    tex: {
        inlineMath: [   // start/end delimiter pairs for in-line math
          ['$', '$'], 
          ['\\(', '\\)'] 
        ],
        displayMath: [  // start/end delimiter pairs for display math
          ['$$', '$$'],
          ['\\[', '\\]']
        ],
        processEscapes: true, // use \$ to produce a literal dollar sign
        macros: { // define your own commands here
          indep: "{\\perp \\!\\!\\! \\perp}",
        },
        tags: 'ams',
      },
  
    svg: {
        fontCache: 'global'
    },
  
    tex2jax: {
        inlineMath: [ ['$','$'], ['\\(','\\)'] ],
        processEscapes: true, 
    },
};