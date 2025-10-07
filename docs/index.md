<style>
  /* Import Cooper Black font */
  @import url('https://fonts.cdnfonts.com/css/cooper-black');
  
  /* Hide everything except our coming soon page */
  html, body {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    height: 100vh !important;
  }
  
  .md-header,
  .md-sidebar,
  .md-nav,
  .md-footer,
  .md-content__inner > :not(.spinney-container) {
    display: none !important;
  }
  
  .md-main__inner {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh !important;
  }
  
  .md-content {
    max-width: 100% !important;
    height: 100vh !important;
  }
  
  .md-content__inner {
    height: 100vh !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  
  /* Video background */
  #bg-video {
    position: fixed;
    top: 50%;
    left: 50%;
    min-width: 100vw;
    min-height: 100vh;
    width: auto;
    height: auto;
    transform: translate(-50%, -50%);
    z-index: 0;
    object-fit: cover;
  }
  
  /* Coming soon page styling - NO SCROLL, perfect centering */
  .spinney-container {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    padding: 0;
    margin: 0;
    text-align: center;
    overflow: hidden;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
  }
  
  .spinney-image-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 3vh;
    position: relative;
    z-index: 10;
  }
  
  .spinney-image {
    width: 33.33vw;
    max-width: 600px;
    min-width: 200px;
    height: auto;
    animation: float 6s ease-in-out infinite;
    filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.4));
  }
  
  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
  }
  
  .spinney-message {
    font-family: 'Cooper Black', 'Impact', 'Arial Black', sans-serif;
    font-size: 10vw;
    font-weight: 900;
    line-height: 1.1;
    width: 100%;
    padding: 0 5vw;
    letter-spacing: 0.02em;
    color: #ffffff;
    text-shadow: 
      0 4px 12px rgba(0, 0, 0, 0.2),
      0 2px 6px rgba(0, 0, 0, 0.15),
      0 1px 3px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    cursor: default;
    position: relative;
    z-index: 10;
  }
  
  .spinney-message:hover {
    transform: scale(1.02);
    text-shadow: 
      0 5px 15px rgba(0, 0, 0, 0.2),
      0 3px 8px rgba(0, 0, 0, 0.15),
      0 1px 4px rgba(0, 0, 0, 0.1);
  }
  
  /* Video attribution */
  .video-credit {
    position: fixed;
    bottom: 10px;
    right: 10px;
    font-size: 8px;
    color: rgba(255, 255, 255, 0.5);
    z-index: 20;
    font-family: Arial, sans-serif;
  }
  
  .video-credit a {
    color: rgba(255, 255, 255, 0.6);
    text-decoration: none;
  }
  
  .video-credit a:hover {
    color: rgba(255, 255, 255, 0.9);
  }
  
  /* Responsive text sizing - keep it as large as possible */
  @media (max-width: 1800px) {
    .spinney-message { font-size: 9vw; }
  }
  
  @media (max-width: 1400px) {
    .spinney-message { font-size: 8vw; }
  }
  
  @media (max-width: 1000px) {
    .spinney-message { font-size: 7vw; }
  }
  
  @media (max-width: 768px) {
    .spinney-message { font-size: 8vw; }
    .spinney-image {
      width: 50vw;
      min-width: 180px;
    }
  }
  
  @media (max-width: 480px) {
    .spinney-message { font-size: 9vw; }
    .spinney-image {
      width: 60vw;
      min-width: 150px;
    }
  }
</style>

<video id="bg-video" autoplay loop muted playsinline>
  <source src="assets/video/groovey01.mp4" type="video/mp4">
</video>

<div class="spinney-container">

<div class="spinney-image-wrapper">
  <img src="assets/images/spinney_groovey.png" alt="Spinney" class="spinney-image">
</div>

<div class="spinney-message">
Spinney Sez:<br>
Stay Groovy!<br>
We're not quite ready yet!
</div>

</div>

<div class="video-credit">
  Video by <a href="https://www.pexels.com/video/colors-blurring-and-moving-11368306/" target="_blank">Tobias Matthews</a>
</div>
