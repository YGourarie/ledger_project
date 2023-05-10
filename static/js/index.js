function setActiveNavItem() {
    // Get the current URL path
    let path = window.location.pathname;
  
    // Get all navbar items
    let navItems = document.querySelectorAll('.nav-item');
  
    // Iterate through the navbar items
    navItems.forEach(function(item) {
      // Get the link element within the navbar item
      let link = item.querySelector('a');
  
      // If the link's href matches the current URL path, set the navbar item as active
      if (link.getAttribute('href') === path) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }

window.onload = setActiveNavItem;
window.onpopstate = setActiveNavItem;
console.log('test')
