(()=>{
  let reviews_div = document.querySelector('[aria-label="Recommended Reviews"] .list__09f24__gE1oR');
  
  let buffer = [];
  
  reviews_div.querySelectorAll('li').forEach(li=>{
    
    let stars_div = li.querySelector('[aria-label$="star rating"]');
    if(!stars_div) return;
    let stars = stars_div.getAttribute('aria-label').split(' ').shift();
    let comment = li.querySelector('p.comment__09f24__RPzvj').innerText;
    
    buffer.push(`=============\n${stars}\n----------\n${comment.trim()}\n`);
    
  });
  
  console.log(buffer.join("\n"));
})();