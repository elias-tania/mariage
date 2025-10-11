

<template>
  <div>
    <Carousel class="home-image" :images="carouselImages"/>
    <div class="container"> 
      <h3>Vous êtes invité.e</h3>
      <p>Nous serions ravis de vous compter parmi nous le jour J. Merci de nous confirmer votre présence grâce au lien ci dessous</p>
      <router-link to="/inscription" class="btn"> S'inscrire</router-link>
    </div>
  </div>
</template>

<script>
import Carousel from './Carousel.vue';

export default {
  name: 'Home',
  components: { Carousel },
  data() {
    return {
      carouselImages: [
        "/src/assets/IMG_3952.jpg",
        "/src/assets/IMG_3977.jpg",
        "/src/assets/IMG_3991.jpg",
        "/src/assets/IMG_3995.jpg",
        "/src/assets/IMG_4034.jpg",
        "/src/assets/IMG_4042.jpg",
        "/src/assets/IMG_4048.jpg",
        "/src/assets/IMG_4083.jpg"
      ]
    };
  }
};

</script>

