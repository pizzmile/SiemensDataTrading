import express from 'express'
import { Op, where } from 'sequelize'
import initializeDatabase from '../db-conn'
const app = express()

const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: true }))
async function init() {
  // Call the init function that returns the Database
  const db = await initializeDatabase()
  // Let's extract all the objects we need to perform queries inside the endpoints
  const { Area, User, Device, EnergyConsumption, Policies } = db._tables

  app.get('/areas', async (req, res) => {
    const areas = await Area.findAll({
      order: [['title', 'ASC']],
    })
    return res.json(areas)
  })

  app.get('/devices', async (req, res) => {
    const devices = await Device.findAll({
      order: [['idDevice', 'ASC']],
    })
    return res.json(devices)
  })

  app.get('/users', async (req, res) => {
    const users = await User.findAll({})
    return res.json(users)
  })

  app.get('/energyconsumptions', async (req, res) => {
    const energyconsumption = await EnergyConsumption.findAll({
      include: { model: Device },
    })
    return res.json(energyconsumption)
  })

  app.get('/policies', async (req, res) => {
    const policies = await Policies.findAll({
      order: [['policyId', 'ASC']],
    })
    return res.json(policies)
  })
  app.post('/createpolicy', async (req, res) => {
    let currentValue = false
    let voltageValue = false
    let apValue = false
    let rpValue = false
    let appValue = false
    let samplesValue = false

    if (req.body.current) {
      currentValue = true
    }
    if (req.body.voltage) {
      voltageValue = true
    }
    if (req.body.activepower) {
      apValue = true
    }
    if (req.body.reactivepower) {
      rpValue = true
    }
    if (req.body.apparentpower) {
      appValue = true
    }
    if (req.body.samples) {
      samplesValue = true
    }

    Policies.truncate()
    await Policies.create({
      current: currentValue,
      voltage: voltageValue,
      activepower: apValue,
      reactivepower: rpValue,
      apparentpower: appValue,
      samples: samplesValue,
    })
  })

  app.post('/updatedeviceactivity', async (req, res) => {
    let devices = await Device.findAll({})
    devices = devices.length

    for (let i = 0; i < devices; i++) {
      await Device.update(
        {
          active: 'false',
        },
        {
          where: { active: 1 },
        }
      )
    }
    for (let i = 0; i < Object.keys(req.body).length; i++) {
      await Device.update(
        {
          active: 'true',
        },
        {
          where: { name: Object.keys(req.body)[i] },
        }
      )
    }
  })
}

init()

export default app
