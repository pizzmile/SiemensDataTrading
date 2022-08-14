<template>
  <footer class="footer" id="footer-element">
    <div class="footer-left-column">
      <span class="show-desktop">
        <img src="~/assets/logo-txt.png" class="footerimg" />
      </span>
    </div>

    <div class="footer-right-column">
      <div class="single-column">
        <div class="column-title">GET IN TOUCH</div>
        <div class="column-subtitle">LINKS</div>

        <div
          v-for="(item, itemIndex) of menuOptions"
          :key="'menu-item-' + itemIndex"
          class="column-text"
        >
          <nuxt-link :to="item.path">
            {{ item.name }}
          </nuxt-link>
        </div>
      </div>

      <div class="single-column">
        <div class="column-title">CONTACT US</div>
        <div class="column-subtitle">HEADQUARTERS</div>
        <div class="column-text">
          <a
            href="http://maps.google.com/?q=1200 Pennsylvania Ave SE, Washington, District of Columbia, 20003"
            target="_blank"
            >231 Gotham Square - 89<br />
            GM Metropolis city</a
          >
          <br />Phone : <a href="tel:+00 123 456 78">+00 123 456 78</a> <br />
          Mail : <a href="mailto:info@hextech.com">info@dalink.com</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import GoToMixins from '~/mixins/goTo-mixins.js'

export default {
  mixins: [GoToMixins],
  data() {
    return {
      menuOptions: [
        {
          name: 'Home',
          path: '/home',
        },
        {
          name: 'Settings',
          path: '/settings',
        },
        {
          name: 'Partners',
          path: '/partners',
        },
      ],
    }
  },
}
</script>

<style scoped>
.footerimg {
  padding: 100px;
  width: 50%;
}

.footer {
  height: 290px;
  background: var(--cc-base5);
  width: 100%;
  display: flex;
  position: relative;
}

.footer-left-column {
  position: absolute;
  bottom: 0;
  left: 130px;
}
.footer-right-column {
  width: 1110px;
  margin: auto;
  padding-top: 80px;
  text-align: right;
  display: flex;
  margin-top: 0;
}
.single-column {
  width: max-content;
  text-align: left;
  margin-left: 50px;
}

.single-column:first-child {
  margin-left: auto;
}
.column-title {
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 17px;
  text-transform: uppercase;
  color: #3d3d3d;
  margin-bottom: 6px;
}
.column-subtitle {
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 22px;
  text-transform: uppercase;
  color: #4d41c9;
  margin-bottom: 18px;
}
.column-text {
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 30px;
  color: #3d3d3d !important;
  mix-blend-mode: normal;
}
.group-name-list {
  list-style: none;
}
a {
  color: #3d3d3d !important;
  text-decoration: none;
  opacity: 0.8;
}
.show-mobile {
  display: none;
}
.show-tablet {
  display: none;
}
.nuxt-link-active {
  color: #4d41c9 !important;
  opacity: 1;
}
@media screen and (max-width: 1200px) {
  .footer {
    height: 196px;
  }
  .footer-right-column {
    padding-top: 26px;
    padding-right: 26px;
    width: auto;
  }
  .footer-left-column {
    position: relative;
    width: max-content;
    left: unset;
    margin: auto;
    text-align: center;
  }
  .single-column {
    margin-left: 65px;
  }
  .single-column:first-child {
    margin-left: auto;
  }
  .single-column:last-child {
    margin-right: auto;
  }
  .column-title {
    font-size: 12px;
    line-height: 14px;
    margin-bottom: 9px;
  }
  .column-subtitle {
    font-size: 13px;
    line-height: 16px;
    margin-bottom: 11px;
  }
  .column-text {
    font-size: 12px;
    line-height: 14px;
  }
}

@media screen and (max-width: 768px) {
  .footer {
    height: 121px;
  }
  .footer-right-column {
    width: 100%;
    padding-top: 45px;
  }
  .footer-left-column {
    width: 100%;
    position: absolute;
  }
  .single-column {
    display: none;
  }
  .column-title {
    font-size: 6px;
    line-height: 7px;
    margin-bottom: 3px;
  }
  .column-subtitle {
    font-size: 6px;
    line-height: 7px;
    margin-bottom: 9px;
  }
  .column-text {
    font-size: 6px;
    line-height: 7px;
  }

  .single-column:last-child {
    display: block;
    margin-right: 0px;
    text-align: center;
    margin-left: auto;
  }
}
</style>
