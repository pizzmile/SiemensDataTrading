<template>
  <main class="container">
    <div class="policy-settings">
      <div class="pre_title">Policy options</div>
      <div class="description">
        Select the data you want to share over the platform
      </div>
      <form action="/api/createpolicy" method="post">
        <input id="current" name="current" type="checkbox" />
        <label for="current"> Current</label><br /><br />

        <input id="voltage" name="voltage" type="checkbox" />
        <label for="voltage"> Voltage</label><br /><br />

        <input id="activepower" name="activepower" type="checkbox" />
        <label for="activepower"> Active Power </label><br /><br />

        <input id="reactivepower" name="reactivepower" type="checkbox" />
        <label for="reactivepower"> Reactive Power </label><br /><br />

        <input id="apparentpower" name="apparentpower" type="checkbox" />
        <label for="apparentpower"> Apparent Power</label><br /><br />

        <input id="samples" name="samples" type="checkbox" />
        <label for="samples"> Samples </label><br /><br />

        <input id="submit" type="submit" value="submit" />
      </form>
    </div>
    <div class="system-settings">
      <div class="pre_title">System options</div>
      <div class="description">
        Manage the functionalities of yout IoT devices
      </div>
      <form>
        <input id="checkbox1" type="checkbox" />
        <label for="checkbox1"> Option 1</label><br /><br />
        <input id="checkbox2" type="checkbox" />
        <label for="checkbox2"> Option 2</label><br /><br />
        <input id="checkbox3" type="checkbox" />
        <label for="checkbox3"> Option 3</label><br /><br />
        <input id="checkbox4" type="checkbox" />
        <label for="checkbox4"> Option 4</label><br /><br />
        <input id="checkbox5" type="checkbox" />
        <label for="checkbox5•"> Option 5</label><br /><br />
      </form>
    </div>
  </main>
</template>

<script>
import GoToMixins from '~/mixins/goTo-mixins.js'

export default {
  components: {},

  mixins: [GoToMixins],

  data() {
    return {
      carouselProp: {},
    }
  },

  head() {
    return {
      title: 'Settings',
    }
  },

  mounted() {},

  methods: {
    scrollRight() {
      const carousel = document.querySelector("[data-target='carousel']")

      if (this.carouselProp.offset > this.carouselProp.maxX) {
        this.carouselProp.offset -=
          this.carouselProp.carouselWidth + this.carouselProp.cardMarginRight
        carousel.style.transform = `translateX(${
          this.carouselProp.offset / 3
        }px)`
      }
    },
    scrollLeft() {
      const carousel = document.querySelector("[data-target='carousel']")
      if (this.carouselProp.offset !== 0) {
        this.carouselProp.offset +=
          this.carouselProp.carouselWidth + this.carouselProp.cardMarginRight
        carousel.style.transform = `translateX(${
          this.carouselProp.offset / 3
        }px)`
      }
    },
    postPolicies() {},
  },
}
</script>

<style scoped>
.container {
  max-width: 100%;
  margin-top: 0;
  overflow: hidden;
  height: 100vh;
}

.head-image {
  display: none;
}

.background {
  width: 100%;
  background: linear-gradient(
    360deg,
    #fcfcff 72.4%,
    rgba(252, 252, 255, 0) 100%
  );
}

.first-paragraph {
  position: relative;
  margin: auto;
  margin-top: 133px;
  height: 1085px;
  width: 1110px;
}

.pre_title {
  text-align: left;
  font-size: 25px;
  text-transform: uppercase;
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;

  /* identical to box height */
  text-transform: uppercase;

  color: #424272;
}

.policy-settings {
  margin: 50px;
  text-align: left;
}

.system-settings {
  margin: 50px;
  text-align: left;
}

.title {
  text-align: left;
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;

  color: #3d3d3d;
}

.subtitle {
  text-align: left;
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;
  margin-bottom: 88px;
  color: #cdc9ff;
}

.descriptions {
  position: relative;
}

.description-1 {
  text-transform: none;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  text-align: left;
  height: 610px;
  width: 350px;
  color: #464a52;

  mix-blend-mode: normal;
  opacity: 0.8;
}

.description-flower {
  display: none;
}

.description-2 {
  text-transform: none;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  text-align: left;
  height: 168px;
  width: 350px;
  color: #464a52;
  position: absolute;
  top: 0;
  left: 40%;

  mix-blend-mode: normal;
  opacity: 0.8;
}

.omino {
  position: absolute;
  bottom: 0;
  right: 0;
}

.second-paragraph {
  position: relative;
  right: 0%;
  margin: auto;
  margin-top: 133px;
  height: 927px;
  width: 1110px;
}

.second-paragraph-contents {
  position: absolute;
  right: 0;
}

.pre_title-2 {
  text-align: right;
  font-size: 25px;
  text-transform: uppercase;

  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  /* identical to box height */
  text-transform: uppercase;

  color: #424272;
}

.title-2 {
  text-align: right;
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;

  color: #424272;
}

.subtitle-2 {
  text-align: right;
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;
  margin-bottom: 88px;
  color: #cdc9ff;
}

.description {
  text-transform: none;
  margin-bottom: 25px;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  text-align: left;
  color: #464a52;
  mix-blend-mode: normal;
  opacity: 0.8;
}

.description-2-2 {
  position: absolute;
  right: 0;
  top: 250%;
  text-transform: none;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  text-align: right;
  color: #464a52;
  width: 350px;
  height: 610px;
  mix-blend-mode: normal;
  opacity: 0.8;
}

.image {
  position: absolute;
  top: 200px;
  left: 0;
}

.background-3 {
  width: 100%;
  padding-top: 75px;
  background: linear-gradient(
    360deg,
    rgba(252, 252, 255, 0) 10.42%,
    #fcfcff 30.21%
  );
}

.third-paragraph-contents {
  text-align: center;
}

.pre_title-3 {
  font-size: 25px;
  text-transform: uppercase;

  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  /* identical to box height */
  text-transform: uppercase;

  color: #424272;
}

.title-3 {
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;

  color: #424272;
}

.subtitle-3 {
  font-size: 60px;
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-transform: uppercase;
  margin-bottom: 88px;
  color: #cdc9ff;
}

.description-3 {
  margin: auto;
  text-transform: none;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  color: #464a52;
  width: 769px;
  height: 123px;
  mix-blend-mode: normal;
  opacity: 0.8;
}

.member-grid-container {
  overflow: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.member-grid-container::-webkit-scrollbar {
  display: none;
}

.member-grid {
  display: grid;
  position: relative;
  width: 1110px;
  grid-template-columns: repeat(4, 1fr);
  margin: auto;
  margin-top: 50px;
}

.team-button {
  cursor: pointer;
  border-style: none;
  background: #e8e6ff;
  border-radius: 35px;
  text-transform: uppercase;
  width: 183px;
  height: 34px;
  margin: auto;
  font-size: 12px;
  line-height: 14px;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: auto;
}

.flower {
  margin-bottom: 153px;
}

.partner-grid {
  position: relative;
  height: 350px;
  width: 1110px;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
  margin: auto;
  margin-top: 50px;
}

.partner {
  margin: auto;
}

.partner-img {
  width: 162px;
  height: 162px;
}

.partner-name {
  margin-top: 30px;
  font-style: normal;
  font-weight: 700;
  font-size: 22px;
  line-height: 26px;
  text-align: center;

  color: #424272;
}

.partner-description {
  font-style: normal;
  font-weight: 300;
  font-size: 18px;
  line-height: 24px;
  margin-top: 11px;
  margin-bottom: 26px;
  text-align: center;

  color: #464a52;
}

.partner-website {
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 24px;
  cursor: pointer;
  text-align: center;
  text-decoration-line: underline;
  color: #4d41c9 !important;
  mix-blend-mode: normal;
  opacity: 0.8;
}

.partner-list-wrapper {
  height: 650px;
  width: 1110px;
  position: relative;
  overflow: hidden;
  margin: 0 auto;
  min-width: 1110px;
}
.partner-carousel {
  margin: 0;
  padding: 0;
  list-style: none;
  width: 100%;
  display: flex;
  position: absolute;
  left: 0;
  transition: all 1s ease;
}
.partner-card {
  min-width: 350px;
  display: inline-block;
}

.partner {
  margin-right: 15px;
  margin-left: 15px;
}
.partner-carousel div:first-child {
  margin-left: 0px;
}
.carousel-wrapper {
  max-width: max-content;
  display: flex;
  align-items: center;
  margin: auto;
}

.carousel-arrow-left {
  position: absolute;
  left: -5px;
  top: 100px;
  cursor: pointer;
  z-index: 1;
}

.carousel-arrow-right {
  position: absolute;
  right: 0;
  top: 100px;
  cursor: pointer;
}

h2 {
  margin-bottom: 30px;
}
h4 {
  margin-bottom: 30px;
}
img {
  max-width: 600px;
}
p {
  text-align: left;
}

@media screen and (max-width: 1200px) {
  .head-image {
    display: initial;
    position: absolute;
    top: 0;
    left: 0;
  }

  .first-paragraph {
    position: relative;
    margin: auto;
    margin-top: 28px;
    height: max-content;
    width: 550px;
  }

  .pre_title {
    text-align: center;
    font-size: 20px;
    line-height: 24px;
    margin-top: 80px;
  }

  .title {
    font-weight: 700;
    font-size: 36px;
    line-height: 43px;
    text-align: center;
  }

  .subtitle {
    font-weight: 700;
    font-size: 36px;
    line-height: 43px;
    text-align: center;
    margin-bottom: 41px;
  }

  .descriptions {
    height: max-content;
    width: 550px;
  }

  .description-1 {
    font-size: 18px;
    line-height: 22px;
    height: max-content;
    width: 550px;
    text-align: center;
  }

  .description-flower {
    display: block;
  }

  .description-2 {
    font-size: 18px;
    line-height: 22px;
    width: 550px;
    height: max-content;
    position: initial;
    margin-top: 14px;
    text-align: center;
  }

  .omino {
    margin-top: 40px;
    position: initial;
    width: 100%;
  }

  .second-paragraph {
    height: max-content;
    width: 550px;
    margin-top: 36px;
  }

  .second-paragraph-contents {
    position: inherit;
    min-height: max-content;
  }

  .pre_title-2 {
    text-align: center;
    margin-bottom: 17px;

    font-size: 20px;
    line-height: 24px;
  }

  .title-2 {
    font-size: 36px;
    line-height: 43px;
    text-align: center;
  }

  .subtitle-2 {
    font-size: 36px;
    line-height: 43px;
    text-align: center;
    margin-bottom: 38px;
  }

  .description-2-1 {
    position: inherit;
    text-transform: none;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    text-align: center;
    color: #464a52;
    width: 550px;
    height: max-content;
    mix-blend-mode: normal;
    opacity: 0.8;
  }

  .description-2-2 {
    position: inherit;
    text-transform: none;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    text-align: center;
    color: #464a52;
    width: 550px;
    height: max-content;
    mix-blend-mode: normal;
    opacity: 0.8;
  }

  .image {
    display: none;
  }

  .background-3 {
    margin-top: 75px;
  }

  .pre-title-3 {
    line-height: 29px;
    font-size: 20px;
    line-height: 24px;
  }

  .title-3 {
    margin-top: 17px;
    font-weight: 700;
    font-size: 36px;
    line-height: 43px;
  }

  .subtitle-3 {
    font-weight: 700;
    font-size: 36px;
    line-height: 43px;
    margin-bottom: 17px;
  }

  .description-3 {
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    width: 550px;
    height: max-content;
  }

  .flower {
    margin-bottom: 30px;
    transform: scale(0.5);
  }

  .member-grid {
    display: grid;
    position: relative;
    width: 646px;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 10px;
  }

  .member-mini {
    margin-bottom: 30px;
  }

  .partner-grid {
    width: 100%;
    height: max-content;
    grid-template-columns: repeat(3, 1fr);
  }

  .partner-carousel {
    overflow: scroll;
    padding: 15px 0;
    width: 100%;
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .carousel-arrow-right {
    display: none;
  }

  .carousel-arrow-left {
    display: none;
  }

  .partner-list-wrapper {
    height: 400px;
    width: 100%;
    min-width: 100%;
  }

  .carousel-wrapper {
    max-width: 100%;
    height: max-content;
  }

  .partner {
    margin-right: 0;
    height: max-content;
  }

  .partner-img {
    width: 200px;
    height: auto;
    margin: auto;
  }
}

@media screen and (max-width: 768px) {
  .head-image {
    display: initial;
    width: 100%;
  }

  .first-paragraph {
    position: relative;
    margin: auto;
    margin-top: 28px;
    height: max-content;
    width: 272px;
  }

  .pre_title {
    text-align: center;
    font-size: 12px;
    line-height: 14px;
  }

  .title {
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    text-align: center;
  }

  .subtitle {
    font-weight: 700;
    font-size: 24px;
    line-height: 29px;
    text-align: center;
    margin-bottom: 17px;
  }

  .descriptions {
    height: max-content;
    width: 272px;
  }

  .description-1 {
    font-size: 16px;
    line-height: 14px;
    height: max-content;
    width: 272px;
  }

  .description-flower {
    display: block;
  }

  .description-2 {
    font-size: 14px;
    line-height: 14px;
    width: 272px;
    position: initial;
    margin-top: 14px;
  }

  .omino {
    position: initial;
    width: 100%;
  }

  .second-paragraph {
    height: max-content;
    width: 272px;
    margin-top: 36px;
  }

  .second-paragraph-contents {
    position: inherit;
    min-height: max-content;
  }

  .pre_title-2 {
    text-align: center;
    margin-bottom: 17px;
  }

  .title-2 {
    font-size: 24px;
    line-height: 29px;
    text-align: center;
  }

  .subtitle-2 {
    font-size: 24px;
    line-height: 29px;
    text-align: center;
    margin-bottom: 38px;
  }

  .description-2-1 {
    position: inherit;
    text-transform: none;
    font-style: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: 14px;
    color: #464a52;
    width: 272px;
    height: max-content;
    mix-blend-mode: normal;
    opacity: 0.8;
  }

  .description-2-2 {
    position: inherit;
    text-transform: none;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 14px;
    color: #464a52;
    width: 272px;
    height: max-content;
    mix-blend-mode: normal;
    opacity: 0.8;
  }

  .image {
    display: none;
  }

  .background-3 {
    margin-top: 50px;
  }

  .title-3 {
    margin-top: 17px;
    font-size: 24px;
    line-height: 29px;
  }

  .subtitle-3 {
    font-size: 24px;
    line-height: 29px;
    margin-bottom: 17px;
  }

  .description-3 {
    font-size: 12px;
    line-height: 14px;
    width: 272px;
  }

  .flower {
    margin-bottom: 30px;
    transform: scale(0.5);
  }

  .member-grid {
    display: grid;
    position: relative;
    width: 375px;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 10px;
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .member-mini {
    margin-bottom: 20px;
  }
  .partner-carousel {
    overflow: scroll;
    padding: 15px 0;
    width: 100%;
    -ms-overflow-style: none;
    scrollbar-width: none;
  }

  .carousel-arrow-right {
    display: none;
  }

  .carousel-arrow-left {
    display: none;
  }

  .partner-list-wrapper {
    height: 400px;
    width: 500%;
  }

  .carousel-wrapper {
    max-width: 100%;
    margin: 0;
  }

  .partner {
    margin-right: 0;
  }

  .partner-card {
    min-width: 375px;
  }

  .partner-img {
    width: 150px;
    height: 150px;
    margin: auto;
  }
}
</style>
