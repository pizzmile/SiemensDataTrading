<template http-equiv="refresh" content="1">
  <main class="container">
    <div class="home-header">
      <div class="dashboard-container">
        <div class="dashboard-item">
          <p class="dashboard-title">Current</p>
          <Bar :chart-data="currentData" :width="'5%'" :height="'5%'" />
          <div
            class="dashboard-value"
            :class="{ shared: policies.current, unshared: !policies.current }"
          >
            {{ avgCurrent }} A
          </div>
        </div>
        <div class="dashboard-item">
          <p class="dashboard-title">Voltage</p>
          <Bar :chart-data="voltageData" :width="'5%'" :height="'5%'" />
          <p
            class="dashboard-value"
            :class="{ shared: policies.voltage, unshared: !policies.voltage }"
          >
            {{ avgVoltage }} V
          </p>
        </div>
        <div class="dashboard-item">
          <p class="dashboard-title">Active Power</p>
          <Bar :chart-data="apData" :width="'5%'" :height="'5%'" />
          <p
            class="dashboard-value"
            :class="{
              shared: policies.activepower,
              unshared: !policies.activepower,
            }"
          >
            {{ avgAP }} W
          </p>
        </div>
        <div class="dashboard-item">
          <p class="dashboard-title">Reactive Power</p>
          <Bar :chart-data="rpData" :width="'50px'" :height="'50px'" />
          <p
            class="dashboard-value"
            :class="{
              shared: policies.reactivepower,
              unshared: !policies.reactivepower,
            }"
          >
            {{ avgRP }} W
          </p>
        </div>
        <div class="dashboard-item">
          <p class="dashboard-title">Apparent Power</p>
          <Bar :chart-data="appData" :width="'50px'" :height="'50px'" />
          <p
            class="dashboard-value"
            :class="{
              shared: policies.apparentpower,
              unshared: !policies.apparentpower,
            }"
          >
            {{ avgAPP }} W
          </p>
        </div>
        <div class="dashboard-item">
          <p class="dashboard-title">Samples</p>
          <p
            class="dashboard-value"
            :class="{
              shared: policies.samples,
              unshared: !policies.samples,
            }"
          >
            {{ energyconsumptions.length }}
          </p>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { Bar } from 'vue-chartjs/legacy'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import GoToMixins from '~/mixins/goTo-mixins.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  components: { Bar },
  mixins: [GoToMixins],
  async asyncData({ $axios }) {
    const { data } = await $axios.get(`${process.env.BASE_URL}/api/devices`)
    const devices = data
    let energyconsumptions = await $axios.get(
      `${process.env.BASE_URL}/api/energyconsumptions`
    )
    energyconsumptions = energyconsumptions.data

    let policies = await $axios.get(`${process.env.BASE_URL}/api/policies`)
    policies = policies.data[0]

    let avgCurrent = 0
    let avgVoltage = 0
    let avgAP = 0
    let avgRP = 0
    let avgAPP = 0

    for (
      let i = energyconsumptions.length - 1;
      i > energyconsumptions.length - 10 && i >= 0;
      i--
    ) {
      avgCurrent += energyconsumptions[i].current
      avgVoltage += energyconsumptions[i].voltage
      avgAP += energyconsumptions[i].activepower
      avgRP += energyconsumptions[i].reactivepower
      avgAPP += energyconsumptions[i].reactivepower
    }

    avgCurrent = avgCurrent / 10
    avgCurrent = Number(avgCurrent.toPrecision(3))

    avgVoltage = avgVoltage / 10
    avgVoltage = Number(avgVoltage.toPrecision(3))

    avgAP = avgAP / 10
    avgAP = Number(avgAP.toPrecision(3))

    avgRP = avgRP / 10
    avgRP = Number(avgRP.toPrecision(3))

    avgAPP = avgAPP / 10
    avgAPP = Number(avgAPP.toPrecision(3))

    return {
      devices,
      energyconsumptions,
      avgCurrent,
      avgVoltage,
      avgAP,
      avgRP,
      avgAPP,
      policies,
    }
  },
  data() {
    return {
      currentData: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [
          {
            label: '',
            backgroundColor: '#d32d7d',
            data: [1200, 1340, 1332, 1321, 1231, 1533, 1322, 1233, 1632, 1523],
          },
        ],
      },
      voltageData: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [
          {
            label: '',
            backgroundColor: '#d32d7d',
            data: [85, 81, 87, 88, 90, 91, 90, 78, 82, 92],
          },
        ],
      },
      apData: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [
          {
            label: '',
            backgroundColor: '#d32d7d',
            data: [
              12000, 13400, 13320, 13210, 12310, 15330, 13202, 12033, 10632,
              15230,
            ],
          },
        ],
      },
      rpData: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [
          {
            label: '',
            backgroundColor: '#d32d7d',
            data: [
              -12000, -7340, -5332, -3131, -7231, -8533, -5322, -6233, -8632,
              -5523,
            ],
          },
        ],
      },
      appData: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        datasets: [
          {
            label: '',
            backgroundColor: '#d32d7d',
            data: [
              -12000, -7340, -5332, -3131, -7231, -8533, -5322, -6233, -8632,
              -5523,
            ],
          },
        ],
      },
      isPositionFixed: false,
    }
  },
  created() {
    this.$router.push('/home')
  },
  mounted() {
    document.addEventListener('scroll', this.handleScroll)
  },
  destroyed() {
    document.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    moveTo(path) {
      const elem = document.getElementById(path)
      elem.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
        inline: 'nearest',
      })
    },
    handleScroll() {
      const buttonBar = document.getElementsByClassName('button-container')[0]
      if (buttonBar.getBoundingClientRect().top < 90 && !this.isPositionFixed) {
        buttonBar.style.position = 'sticky'
        buttonBar.style.top = '90px'
        this.isPositionFixed = true
      }
      if (buttonBar.getBoundingClientRect().top > 90 && this.isPositionFixed) {
        buttonBar.style.position = 'static'
        buttonBar.style.top = 0
        this.isPositionFixed = false
      }
    },
  },
}
</script>

<style scoped>
.container {
  max-width: 100%;
  padding-top: 0px;
  margin-top: 0px;
  padding: 0;
}
.home-header {
  position: relative;
  overflow-x: clip;
}
.dashboard-container {
  display: grid;
  grid-template-columns: auto auto auto;
  padding-top: 50px;
  width: 100%;
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 800;
  font-size: 32px;
  margin: auto;
  height: 100%;
  color: #4d41c9;
}

.dashboard-item {
  width: 200px;
  margin: auto;
}

.home-header-text {
  text-align: center;
  font-family: 'Poppins', sans-serif;
  font-style: normal;
  font-weight: 800;
  font-size: 96px;
  text-transform: uppercase;
  color: #3d3d3d;
  margin: auto;
  line-height: 100px;
  width: 100%;
  position: absolute;
  top: calc(50% - 100px / 2 + 0.5px);
}
.background-image-header {
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  bottom: 0;
}

.title-purple {
  color: #4d41c9;
}

.dashboard-item {
  padding-bottom: 30px;
}

.text1 {
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  text-transform: uppercase;
  color: var(--cc-base1);
  margin-bottom: 44px;
  padding-top: 152px;
}

.scroll-text-compare {
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  text-transform: uppercase;
  color: var(--cc-base1);
  margin: auto;
  padding: 25px 15px;
}

.section-title {
  font-style: normal;
  font-weight: 700;
  font-size: 70px;
  line-height: 84px;
  text-align: center;
  text-transform: uppercase;
  color: #3d3d3d;
}
.section-title-2 {
  color: var(--cc-violet);
}
.section-description {
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 32px;
  text-align: center;
  color: var(--c-grey1);
  mix-blend-mode: normal;
  opacity: 0.8;
  max-width: 769px;
  margin: auto;
  margin-top: 86px;
  margin-bottom: 86px;
}

.button-container {
  width: 100%;
  margin: auto;
  background: #fff;
  z-index: 1;
  padding: 15px 0;
  background: #fbfbff 79.17%;
}
.button-inner-container {
  display: inline-flex;
  max-width: 1110px;
  margin: auto;
  width: 100%;
  padding-bottom: 15px;
}

.dashboard-value {
  background: #f9f9ff;
  border: 2px solid var(--cc-base2);
  border-radius: 35px;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  text-transform: uppercase;
  margin: auto;
  padding: 10px;
  color: #4d41c9;
  width: 80%;
}

.dashboard-value.shared {
  background: #f9f9ff;
  border: 2px solid yellowgreen;
  border-radius: 35px;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  text-transform: uppercase;
  margin: auto;
  padding: 10px;
  color: #4d41c9;
  width: 80%;
}

.dashboard-value.unshared {
  background: #f9f9ff;
  border: 2px solid red;
  border-radius: 35px;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  text-transform: uppercase;
  margin: auto;
  padding: 10px;
  color: #4d41c9;
  width: 80%;
}

.go-to-area-button:hover {
  background: var(--cc-base2);
  color: white;
  cursor: pointer;
  opacity: 1;
}
.area-visibile-button {
  background: var(--cc-base1);
  color: white;
  cursor: pointer;
  opacity: 0.7;
}
.areas-container {
  background: linear-gradient(
    180deg,
    #fbfbff 79.17%,
    rgba(251, 251, 255, 0) 100%
  );
}
.areas-inner-container {
  max-width: 1110px;
  margin: auto;
}
.single-area-section {
  display: table;
  margin: auto;
  scroll-margin-top: 70px;
}
.show-only-tablet-mobile {
  display: none;
}
@media screen and (max-width: 1200px) {
  .home-header {
    height: 250px;
  }
  .home-header-text {
    font-size: 24px;
  }
  .text1 {
    font-size: 20px;
    line-height: 24px;
    margin-bottom: 17px;
    padding-top: 33px;
  }
  .section-title {
    font-size: 36px;
    line-height: 43px;
  }
  .section-description {
    font-size: 18px;
    line-height: 22px;
    margin-top: 21px;
    margin-bottom: 60px;
  }
  .areas-container {
    width: 100%;
    padding-left: 71px;
    padding-right: 71px;
  }
  .button-container {
    display: none;
  }
  .show-only-tablet-mobile {
    display: block;
  }
  .single-area-section {
    width: 100%;
  }
  .single-area-section:last-child > .show-only-tablet-mobile {
    display: none;
  }
}

@media screen and (max-width: 768px) {
  .home-header {
    height: 165px;
  }
  .background-image-header {
    bottom: -20px;
  }
  .text1 {
    font-size: 12px;
    line-height: 14px;
    padding-top: 39px;
  }
  .section-title {
    font-size: 24px;
    line-height: 29px;
  }
  .section-description {
    font-size: 12px;
    line-height: 14px;
    margin-top: 17px;
    margin-bottom: 39px;
  }
  .areas-container {
    width: 100%;
    padding-left: 50px;
    padding-right: 50px;
  }
}
</style>
