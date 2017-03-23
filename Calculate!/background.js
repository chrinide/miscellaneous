/**
 * Listens for the app launching then creates the window
 *
 * @see http://developer.chrome.com/apps/app.window.html
 */
chrome.extension.runtime.onLaunched.addListener(function() {
  chrome.extension.window.create('index.html', {
    id: 'main',
    bounds: { width: 400, height: 400 }
  });
});