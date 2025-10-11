<template>
  <div class="carousel">
    <img :src="images[currentIndex]" :alt="'Image ' + (currentIndex + 1)" class="carousel-image"/>
  </div>
</template>

<script>
export default {
  name: "Carousel",
  props: {
    images: {
      type: Array,
      required: true
    },
    interval: {
      type: Number,
      default: 10000 // 3 secondes
    }
  },
  data() {
    return {
      currentIndex: 0,
      timer: null
    };
  },
  mounted() {
    this.startAutoSlide();
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
  methods: {
    startAutoSlide() {
      this.timer = setInterval(() => {
        this.nextImage();
      }, this.interval);
    },
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    prevImage() {
      this.currentIndex =
        (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
    goToImage(index) {
      this.currentIndex = index;
    }
  }
};
</script>
