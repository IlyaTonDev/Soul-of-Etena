const referralButton = document.querySelector('.referral-button');
const referralPopup = document.querySelector('.referral-popup');
const inviteButton = document.querySelector('.invite-button');

referralButton.addEventListener('click', () => {
  referralPopup.classList.add('show');
});

inviteButton.addEventListener('click', () => {
  // Откройте ссылку приглашения в новом окне
  window.open('https://example.com/referral-link', '_blank');
});

document.addEventListener('click', (e) => {
  if (e.target !== referralPopup && e.target !== referralButton) {
    referralPopup.classList.remove('show');
  }
});
