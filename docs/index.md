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
  
  /* Psychedelic flowing background */
  .spinney-container::before,
  .spinney-container::after {
    content: '';
    position: absolute;
    width: 200vw;
    height: 200vh;
    top: -50vh;
    left: -50vw;
    z-index: 1;
    opacity: 0.6;
  }
  
  .spinney-container::before {
    background: 
      radial-gradient(circle at 20% 30%, rgba(255, 107, 157, 0.4) 0%, transparent 50%),
      radial-gradient(circle at 80% 70%, rgba(108, 92, 231, 0.4) 0%, transparent 50%),
      radial-gradient(circle at 40% 80%, rgba(253, 121, 168, 0.4) 0%, transparent 50%),
      radial-gradient(circle at 60% 20%, rgba(116, 185, 255, 0.4) 0%, transparent 50%),
      radial-gradient(circle at 90% 40%, rgba(253, 203, 110, 0.4) 0%, transparent 50%),
      linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    animation: psychedelicFlow1 30s ease-in-out infinite;
  }
  
  .spinney-container::after {
    background: 
      radial-gradient(circle at 70% 60%, rgba(192, 108, 132, 0.3) 0%, transparent 50%),
      radial-gradient(circle at 30% 40%, rgba(162, 155, 254, 0.3) 0%, transparent 50%),
      radial-gradient(circle at 50% 90%, rgba(255, 118, 117, 0.3) 0%, transparent 50%),
      radial-gradient(circle at 10% 50%, rgba(80, 227, 194, 0.3) 0%, transparent 50%);
    animation: psychedelicFlow2 25s ease-in-out infinite reverse;
  }
  
  @keyframes psychedelicFlow1 {
    0%, 100% { 
      transform: translate(0%, 0%) rotate(0deg) scale(1);
      opacity: 0.6;
    }
    25% { 
      transform: translate(-5%, 5%) rotate(90deg) scale(1.1);
      opacity: 0.7;
    }
    50% { 
      transform: translate(5%, -5%) rotate(180deg) scale(1);
      opacity: 0.6;
    }
    75% { 
      transform: translate(-3%, -3%) rotate(270deg) scale(1.05);
      opacity: 0.7;
    }
  }
  
  @keyframes psychedelicFlow2 {
    0%, 100% { 
      transform: translate(0%, 0%) rotate(0deg) scale(1);
      opacity: 0.5;
    }
    33% { 
      transform: translate(3%, -4%) rotate(120deg) scale(1.15);
      opacity: 0.6;
    }
    66% { 
      transform: translate(-4%, 3%) rotate(240deg) scale(1.05);
      opacity: 0.5;
    }
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
      0 6px 20px rgba(0, 0, 0, 0.4),
      0 3px 10px rgba(0, 0, 0, 0.3),
      0 1px 3px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
    cursor: default;
    position: relative;
    z-index: 10;
  }
  
  .spinney-message:hover {
    transform: scale(1.02);
    text-shadow: 
      0 8px 30px rgba(0, 0, 0, 0.5),
      0 4px 15px rgba(0, 0, 0, 0.4),
      0 2px 5px rgba(0, 0, 0, 0.6);
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
