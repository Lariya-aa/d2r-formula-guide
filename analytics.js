// Vercel Analytics - only loads when @vercel/analytics is available
// Works on Vercel deployment, gracefully skipped on other hosts
(function() {
  if (typeof window !== 'undefined' && window.va) {
    window.va('track', 'pageview');
  }
})();
