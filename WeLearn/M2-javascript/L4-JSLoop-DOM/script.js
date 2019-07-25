const names = ['Alice', 'Bob', 'Charlie', 'Deborah', ' Evan'];
for (i = 0; i < names.length; i++){
  console.log(names[i]);
}
const numbers = ['1','2','3','4','5','6','7','8','9'];
for (i = 0; i < 5; i++){
  console.log(numbers[i]);
}
names.forEach((names) => {
  console.log(names);
})
const books = ['Harry potter', 'Lightning Thief', 'Diary of a wimpy kid', 'Hunger Games', ' Ready Player One'];
for (i = 0; i < books.length; i++){
  console.log("I really Love " + books[i]);
}

let sum = 0;
let numbersadd = [1,2,3,4,5,6,7,8,9];

for (i = 0; i < numbersadd.length; i++){
  sum = sum + numbersadd[i];
}
console.log(sum);


let sum2 = 0;
let list = [1,2,3,4];
const findTotal = (list) => {
  sum2 = sum2 + list;
}
list.forEach(findTotal);

const buttons = document.querySelectorAll('button');
const box = document.querySelector('#box');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const color = button.innerHTML;
      box.style.background = color;
    });
});
