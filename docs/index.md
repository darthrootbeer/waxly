<style>
  /* Hide everything except our coming soon page */
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
  }
  
  .md-content {
    max-width: 100% !important;
  }
  
  /* Coming soon page styling */
  .spinney-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    padding: 2rem;
    text-align: center;
  }
  
  .spinney-image {
    max-width: 600px;
    width: 90%;
    height: auto;
    margin-bottom: 3rem;
    animation: float 6s ease-in-out infinite;
  }
  
  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
  }
  
  .spinney-message {
    font-family: 'New York Medium', 'Georgia', serif;
    font-size: 200px;
    font-weight: 500;
    line-height: 1.2;
    background: linear-gradient(45deg, #ff6b9d, #c06c84, #6c5ce7, #a29bfe, #fd79a8, #fdcb6e, #ff7675, #74b9ff);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 4px 20px rgba(255, 107, 157, 0.3);
    animation: psychedelic 8s ease infinite;
    transition: all 0.3s ease;
    cursor: default;
  }
  
  .spinney-message:hover {
    animation: shimmer 1.5s ease infinite, psychedelic 8s ease infinite;
    transform: scale(1.02);
    filter: hue-rotate(45deg) brightness(1.1);
  }
  
  @keyframes psychedelic {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  
  @keyframes shimmer {
    0%, 100% { filter: hue-rotate(0deg) brightness(1); }
    25% { filter: hue-rotate(15deg) brightness(1.1); }
    50% { filter: hue-rotate(30deg) brightness(1.2); }
    75% { filter: hue-rotate(15deg) brightness(1.1); }
  }
  
  /* Responsive sizing */
  @media (max-width: 1400px) {
    .spinney-message { font-size: 150px; }
  }
  
  @media (max-width: 1000px) {
    .spinney-message { font-size: 100px; }
  }
  
  @media (max-width: 600px) {
    .spinney-message { font-size: 60px; }
    .spinney-image { max-width: 400px; }
  }
  
  @media (max-width: 400px) {
    .spinney-message { font-size: 40px; }
    .spinney-image { max-width: 300px; }
  }
</style>

<div class="spinney-container" markdown="1">

![Spinney](assets/images/spinney_groovey.png){: .spinney-image }

<div class="spinney-message">
Spinney Sez:<br>
Stay Groovy!<br>
We're not quite ready yet!
</div>

</div>
