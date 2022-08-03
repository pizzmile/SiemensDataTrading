import express from 'express'
import { Op, where } from 'sequelize'
import initializeDatabase from '../db-conn'
const app = express()

// We need this one if we send data inside the body as JSON
app.use(express.json())

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
    await Policies.create({
      duration: false,
      failurerate: false,
      reliability: false,
      workingdevices: false,
      production: false,
      defects: false,
    })
  })
}

init()

export default app