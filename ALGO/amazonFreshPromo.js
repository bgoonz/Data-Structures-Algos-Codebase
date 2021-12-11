/*
  Amazon Fresh Promo (example question)

  Amazon is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.

  Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
  Based on the above secret code list, a customer who made either of the following purchases would win the prize:
  orange, apple, apple, banana, orange, banana
  apple, apple, orange, orange, banana, apple, banana, banana

  Write an algorithm to output 1 if the customer is a winner else output 0.

  Input
  The input to the function/method consists of two arguments:
  codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
  shoppingCart, a list of strings representing the order in which a customer purchases fruit.

  Output
  Return an integer 1 if the customer is a winner else return 0.

  Note
  'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
  'anything' must represent one and only one fruit.
  If secret code list is empty then it is assumed that the customer is a winner.

  Example 1:

  Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
  Output: 1
  Explanation:
  codeList contains two groups - [apple, apple] and [banana, anything, banana].
  The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

  Example 2:

  Input: codeList = [[apple, apple], [banana, anything, banana]]
  shoppingCart = [banana, orange, banana, apple, apple]
  Output: 0
  Explanation:
  The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

  Example 3:

  Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
  Output: 0
  Explanation:
  The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

  Example 4:

  Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
  Output: 0
  Explanation:
  The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.

   * Complete the 'foo' function below.
   *
   * The function is expected to return an INTEGER.
   * The function accepts following parameters:
   *  1. STRING_ARRAY codeList
   *  2. STRING_ARRAY shoppingCart
*/

function hasOrder(shoppingCart, index, order) {
    for (let i = 0; i < order.length; i++) {
        let currentCart = (shoppingCart[index]) ? shoppingCart[index].includes(order[i]) : false;
        if (index < shoppingCart.length && order[i].includes('anything') || currentCart) {
            index++;
        } else {
            return false;
        }
    }
    
    return true;
}

function foo(codeList, shoppingCart) {
    // Write your code here
    let splitCodeList = codeList.map((code) => {
        return code.split(' ');
    });
        
    let cartIndex = 0;
    let codeIndex = 0;
    
    while(cartIndex < shoppingCart.length && codeIndex < splitCodeList.length) {
        let current = shoppingCart[cartIndex];
        if (splitCodeList[codeIndex][0].includes('anything') || splitCodeList[codeIndex][0].includes(current) && hasOrder(shoppingCart, cartIndex, splitCodeList[codeIndex])) {
            cartIndex += splitCodeList[codeIndex++].length;
        } else {
            cartIndex++;
        }
    }
    
    return codeIndex === codeList.length ? 1 : 0;
}