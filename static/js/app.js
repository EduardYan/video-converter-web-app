/**
 * Principal Source.
 */


import { askToDelete } from './utils.js';


/**
 * Principal function for execute
 */
function main() {
  // getting the buttons
  const buttons = document.querySelectorAll('.delete-button')

  buttons.forEach((button) => {
    button.addEventListener('click', (e) => {
      // asking
      if (!askToDelete('You want delete this video.')) {
        e.preventDefault();
      }
    });
  })


}

main();