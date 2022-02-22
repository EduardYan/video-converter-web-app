/**
 * Some utils functions to use.
 */

/**
 * 
 * @param {string} message The message to show for ask
 * @returns The answer give
 */
export const askToDelete = (message) => {
  const answer = confirm(message);
  return answer;
}