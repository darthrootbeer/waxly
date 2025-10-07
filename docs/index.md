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
  
  /* Coming soon page styling - NO SCROLL, perfect centering */
  .spinney-container {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    padding: 0;
    margin: 0;
    text-align: center;
    overflow: hidden;
  }
  
  .spinney-image-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 3vh;
  }
  
  .spinney-image {
    width: 33.33vw;
    max-width: 600px;
    min-width: 200px;
    height: auto;
    animation: float 6s ease-in-out infinite;
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
    background: linear-gradient(45deg, #ff6b9d, #c06c84, #6c5ce7, #a29bfe, #fd79a8, #fdcb6e, #ff7675, #74b9ff);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    -webkit-text-stroke: 0.5px rgba(255, 107, 157, 0.3);
    filter: drop-shadow(0 6px 25px rgba(255, 107, 157, 0.5));
    animation: psychedelic 8s ease infinite;
    transition: all 0.3s ease;
    cursor: default;
  }
  
  .spinney-message:hover {
    animation: shimmer 1.5s ease infinite, psychedelic 8s ease infinite;
    transform: scale(1.02);
    filter: drop-shadow(0 6px 30px rgba(255, 107, 157, 0.6)) hue-rotate(45deg) brightness(1.1);
  }
  
  @keyframes psychedelic {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  
  @keyframes shimmer {
    0%, 100% { 
      filter: drop-shadow(0 4px 20px rgba(255, 107, 157, 0.4)) hue-rotate(0deg) brightness(1); 
    }
    25% { 
      filter: drop-shadow(0 5px 25px rgba(192, 108, 132, 0.5)) hue-rotate(15deg) brightness(1.1); 
    }
    50% { 
      filter: drop-shadow(0 6px 30px rgba(108, 92, 231, 0.6)) hue-rotate(30deg) brightness(1.2); 
    }
    75% { 
      filter: drop-shadow(0 5px 25px rgba(162, 155, 254, 0.5)) hue-rotate(15deg) brightness(1.1); 
    }
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
