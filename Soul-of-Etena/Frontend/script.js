const coin = document.getElementById('coin');
const soulsCount = document.getElementById('souls-count');
let count = 0;

coin.addEventListener('click', () => {
  count++;
  soulsCount.textContent = count;
});
