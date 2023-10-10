function wordPattern(pattern: string, s: string): boolean {
  /**Split the string into words and store them in an array*/
  const words = s.split(" ");
  /**Split characters in pattern and store them in an array*/
  const letters = pattern.split("");
  /**Instantiate the mapping object.
   * The characters will be the keys, while words will be the values.
   */
  const map: object = new Object();
  /**
   * First check is whether the length of the string equates to the length of the array.
   * If not, return false.
   */
  if (letters.length !== words.length) {
    return false;
  }
  /**Iterate over the string characters and check if each character exists in
   * any object in the array
   */
  for (let i = 0; i < letters.length; i++) {
    /**Get a list of the keys*/
    const keys = Object.keys(map);
    /**Get a list of the keys*/
    const values = Object.values(map);
    /**start by checking if the character is already in the map object*/
    if (keys.indexOf(letters[i]) >= 0) {
      /**check if the word in the array is the same as the one stored in the map object*/
      if (words[i] !== map[letters[i]]) {
        return false;
      }
    } else {
      /**First, check if the word in the array is already in the map object*/
      if (values.indexOf(words[i]) >= 0) {
        return false;
      }
      /**If both the character and word are not in the map object, add them to the map object*/
      map[letters[i]] = words[i];
    }
  }
  return true;
}
