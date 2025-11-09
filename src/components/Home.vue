

<template>
  <div>
    <Carousel class="home-image" :images="carouselImages"/>
    <div class="container"> 
      <h3>Vous êtes invité.e</h3>
      <p v-if="$route.query.message" class="status">
        {{ $route.query.message }}
      </p>
      <p>Nous serions ravis de vous compter parmi nous le jour J. Merci de nous confirmer votre présence grâce au lien ci dessous</p>
      <router-link to="/inscription" class="btn"> S'inscrire</router-link>
    </div>
  </div>
</template>

<script>
import Carousel from './Carousel.vue';
import IMG3952 from '../assets/IMG_3952.jpg';
import IMG3977 from '../assets/IMG_3977.jpg';
import IMG3991 from '../assets/IMG_3991.jpg';
import IMG3995 from '../assets/IMG_3995.jpg';
import IMG4034 from '../assets/IMG_4034.jpg';
import IMG4042 from '../assets/IMG_4042.jpg';
import IMG4048 from '../assets/IMG_4048.jpg';
import IMG4083 from '../assets/IMG_4083.jpg';
export default {
  name: 'Home',
  components: { Carousel },
  data() {
    return {
      carouselImages: [
         IMG3952,
          IMG3977,
          IMG3991,
          IMG3995,
          IMG4034,
          IMG4042,
          IMG4048,
          IMG4083,
      ]
    };
  }
};

</script>

