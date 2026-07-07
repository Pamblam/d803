(()=>{ 
  let reviews_div = document.querySelector('[aria-label="Recommended Reviews"] .list__09f24__gE1oR');
  let data = JSON.parse(localStorage.getItem('yerlp') || '[]');
  
  reviews_div.querySelectorAll('li').forEach(li=>{
    
    let stars_div = li.querySelector('[aria-label$="star rating"]');
    if(!stars_div) return;
    let stars = stars_div.getAttribute('aria-label').split(' ').shift();
    let comment = li.querySelector('p.comment__09f24__RPzvj').innerText;
    
    data.push({stars, comment});
    
  });
  
  localStorage.setItem('yerlp', JSON.stringify(data));
  console.clear();
  console.log(`${data.length} reviews`);
  
  let pagination_links = document.querySelector(`[data-testid="pagination-links"]`);
  pagination_links.scrollIntoView();

  if(data.length >= 500){
	document.body.innerHTML = `<textarea style="width:100vw;height:100vh;">${JSON.stringify(data, null, 2)}</textarea>`;
  }
})();