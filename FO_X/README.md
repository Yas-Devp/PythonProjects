<p class="text-center"></p>
<h6 class="text-center"><img title="FO_X icon" alt="FO_X icon" src="https://img.itch.zone/aW1nLzI0MDgyNDI3LnBuZw==/original/CG12eO.png"></h6>
<h6 class="text-center">Title:&nbsp;</h6>
<h2 class="text-center">File Organizer X</h2>
<p><br></p>

[![FO_X on itch.io](https://img.shields.io/badge/FO_X-itch.io-8bc8f4?style=for-the-badge&logo=itch.io)](https://yaspro-dev.itch.io/fo-x)


<h4><strong>Description:</strong></h4>
<p>&nbsp;File Organizer X is a handy program developed in Python that allows you to organize and sort your files quickly and efficiently. With this tool, you can easily categorize and manage your files by type, size, date, and more. Say goodbye to cluttered folders and messy desktops, and start organizing your files with ease today!</p>

<h4> Screenshots : </h4>

<h4>Screenshots:</h4>

<div style="position: relative; width: 100%; max-width: 600px; margin: 20px auto; background: #020019; border-radius: 8px; overflow: hidden;">
  <div style="position: relative; width: 100%; padding-bottom: 150%;">
    <img id="slider-image" src="https://img.itch.zone/aW1hZ2UvNDAzOTYzMS8yNDA5NDE3MC5qcGc=/250x600/VAkr8s.jpg" 
         style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;" alt="FO_X Screenshots">
  </div>
  
  <!-- Navigation Buttons -->
  <button onclick="changeSlide(-1)" style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.7); border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px; font-size: 18px;">❮</button>
  <button onclick="changeSlide(1)" style="position: absolute; right: 10px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.7); border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px; font-size: 18px;">❯</button>
  
  <!-- Indicators -->
  <div style="position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); display: flex; gap: 8px;">
    <span onclick="currentSlide(0)" style="width: 10px; height: 10px; background: white; border-radius: 50%; cursor: pointer;"></span>
    <span onclick="currentSlide(1)" style="width: 10px; height: 10px; background: rgba(255,255,255,0.5); border-radius: 50%; cursor: pointer;"></span>
    <span onclick="currentSlide(2)" style="width: 10px; height: 10px; background: rgba(255,255,255,0.5); border-radius: 50%; cursor: pointer;"></span>
  </div>
</div>

<script>
  const slides = [
    "https://img.itch.zone/aW1hZ2UvNDAzOTYzMS8yNDA5NDE3MC5qcGc=/250x600/VAkr8s.jpg",
    "https://img.itch.zone/aW1hZ2UvNDAzOTYzMS8yNDA5NDE3MS5qcGc=/250x600/7zO2CD.jpg",
    "https://img.itch.zone/aW1hZ2UvNDAzOTYzMS8yNDA5NDE3Mi5qcGc=/250x600/wlCClp.jpg"
  ];
  let currentIndex = 0;
  
  function changeSlide(n) {
    currentIndex = (currentIndex + n + slides.length) % slides.length;
    updateSlider();
  }
  
  function currentSlide(n) {
    currentIndex = n;
    updateSlider();
  }
  
  function updateSlider() {
    document.getElementById('slider-image').src = slides[currentIndex];
    document.querySelectorAll('[onclick*="currentSlide"]').forEach((el, i) => {
      el.style.background = i === currentIndex ? 'white' : 'rgba(255,255,255,0.5)';
    });
  }
</script>

<h4>Key Features:</h4>
<p>- Sort files by type, size, date, and more</p>
<p>- Create custom categories for easy organization</p>
<p>- Intuitive and user-friendly interface</p>
<p>- Supports a wide range of file formats</p>
<p>- Cross-platform compatibility</p>
<h4>Instructions:</h4>
<p>1. Download the File Organizer program&nbsp;</p>
<p>2. Run the program on your computer</p>
<p>3. Select the folder you want to organize</p>
<p>4. Choose the sorting criteria</p>
<p>5. Click the organize button and watch as your files are neatly sorted</p>
<p class="text-center"><strong>Notice</strong> : The program won't work if you don't add its icon on the same path (directory)</p>
<p class="text-center">Get organized with <strong>File Organizer</strong> now!</p>
<p></p>
<p><a href="https://ko-fi.com/loris_" target="_blank"><br> <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me a Coffee" title="Buy Me a Coffee"><br></a></p>
