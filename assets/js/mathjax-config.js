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
        tags: 'ams',
        macros: { // define your own commands here
          indep: "{\\perp \\!\\!\\! \\perp}",
          // bold face capital letter
          bA: "\\boldsymbol{A}",
          bB: "\\boldsymbol{B}",
          bC: "\\boldsymbol{C}",
          bD: "\\boldsymbol{D}",
          bE: "\\boldsymbol{E}",
          bF: "\\boldsymbol{F}",
          bG: "\\boldsymbol{G}",
          bH: "\\boldsymbol{H}",
          bI: "\\boldsymbol{I}",
          bJ: "\\boldsymbol{J}",
          bK: "\\boldsymbol{K}",
          bL: "\\boldsymbol{L}",
          bM: "\\boldsymbol{M}",
          bN: "\\boldsymbol{N}",
          bP: "\\boldsymbol{P}",
          bQ: "\\boldsymbol{Q}",
          bR: "\\boldsymbol{R}",
          bS: "\\boldsymbol{S}",
          bT: "\\boldsymbol{T}",
          bU: "\\boldsymbol{U}",
          bV: "\\boldsymbol{V}",
          bW: "\\boldsymbol{W}",
          bX: "\\boldsymbol{X}",
          bY: "\\boldsymbol{Y}",
          bZ: "\\boldsymbol{Z}",
          
          // bold face lowercase letter
          ba: "\\boldsymbol{a}",
          bb: "\\boldsymbol{b}",
          bc: "\\boldsymbol{c}",
          bd: "\\boldsymbol{d}",
          be: "\\boldsymbol{e}",
          bg: "\\boldsymbol{g}",
          bh: "\\boldsymbol{h}",
          bi: "\\boldsymbol{\\imath}",
          bm: "\\boldsymbol{m}",
          bp: "\\boldsymbol{p}",
          bq: "\\boldsymbol{q}",
          br: "\\boldsymbol{r}",
          bs: "\\boldsymbol{s}",
          bt: "\\boldsymbol{t}",
          bu: "\\boldsymbol{u}",
          bv: "\\boldsymbol{v}",
          bw: "\\boldsymbol{w}",
          bx: "\\boldsymbol{x}",
          by: "\\boldsymbol{y}",

          // math calligraphic font
          Acal: "\\mathcal{A}",
          Bcal: "\\mathcal{B}",
          Ccal: "\\mathcal{C}",
          Dcal: "\\mathcal{D}",
          Ecal: "\\mathcal{E}",
          Fcal: "\\mathcal{F}",
          Gcal: "\\mathcal{G}",
          Hcal: "\\mathcal{H}",
          Ical: "\\mathcal{I}",
          Jcal: "\\mathcal{J}",
          Kcal: "\\mathcal{K}",
          Lcal: "\\mathcal{L}",
          Mcal: "\\mathcal{M}",
          Ncal: "\\mathcal{N}",
          Ocal: "\\mathcal{O}",
          Pcal: "\\mathcal{P}",
          Qcal: "\\mathcal{Q}",
          Rcal: "\\mathcal{R}",
          Scal: "\\mathcal{S}",
          Tcal: "\\mathcal{T}",
          Ucal: "\\mathcal{U}",
          Vcal: "\\mathcal{V}",
          Wcal: "\\mathcal{W}",
          Xcal: "\\mathcal{X}",
          Ycal: "\\mathcal{Y}",
          Zcal: "\\mathcal{Z}",

          

          // uppercase greeks
          bAlpha: "\\boldsymbol{\\Alpha}",
          bBeta: "\\boldsymbol{\\beta}",
          bDelta: "\\boldsymbol{\\delta}",
          bEta: "\\boldsymbol{\\eta}",
          bGamma: "\\boldsymbol{\\Gamma}",
          bLambda: "\\boldsymbol{\\Lambda}",
          bOmega: "\\boldsymbol{\\Omega}",
          bPhi: "\\boldsymbol{\\Phi}",
          bPi: "\\boldsymbol{\\Pi}",
          bPsi: "\\boldsymbol{\\Psi}",
          bSigma: "\\boldsymbol{\\Sigma}",
          bTau: "\\boldsymbol{\\tau}",
          bXi: "\\boldsymbol{\\Xi}",
          
          // lowercase greeks
          bbeta: "\\boldsymbol{\\beta}",
          bdelta: "\\boldsymbol{\\delta}",
          blambda: "\\boldsymbol{\\lambda}",
          bmu: "\\boldsymbol{\\mu}",
          bphi: "\\boldsymbol{\\phi}",
          bpi: "\\boldsymbol{\\pi}",
          bpsi: "\\boldsymbol{\\psi}",
          brho: "\\boldsymbol{\\rho}",
          bsigma: "\\boldsymbol{\\sigma}",
          btau: "\\boldsymbol{\\tau}",
          bxi: "\\boldsymbol{\\xi}", 
          },
      },
  
    svg: {
        fontCache: 'global'
    },
  
    tex2jax: {
        inlineMath: [ ['$','$'], ['\\(','\\)'] ],
        processEscapes: true, 
    },
};