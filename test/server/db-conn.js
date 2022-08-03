const { Sequelize, DataTypes, Op } = require('sequelize')

// Development
const db = new Sequelize('mysql://admin:admin@192.168.1.163:3306/SS_DB', {})
// Production
// const pg = require('pg')
// pg.defaults.ssl = true
// const db = new Sequelize(process.env.DATABASE_URL, {
//   ssl: true,
//   dialectOptions: { ssl: { require: true, rejectUnauthorized: false } },
// })

/**
 * Function to define the structure of the database
 */
function defineDBStructure() {
  const Area = db.define(
    'area',
    {
      title: DataTypes.STRING,
    },
    {
      createdAt: false,
      updatedAt: false,
    }
  )
  const Device = db.define(
    'device',
    {
      idDevice: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
      },
      name: DataTypes.STRING,
      description: DataTypes.STRING,
    },
    {
      createdAt: false,
      updatedAt: false,
    }
  )

  const Policies = db.define(
    'policies',
    {
      policyId: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
      },
      duration: DataTypes.BOOLEAN,
      failurerate: DataTypes.BOOLEAN,
      reliability: DataTypes.BOOLEAN,
      workingdevices: DataTypes.BOOLEAN,
      production: DataTypes.BOOLEAN,
      defects: DataTypes.BOOLEAN,
    },
    {
      createdAt: false,
      updatedAt: false,
    }
  )

  const EnergyConsumption = db.define(
    'energyconsumption',
    {
      sampleId: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
      },
      timestamp: DataTypes.TIME,
      current: DataTypes.FLOAT,
      voltage: DataTypes.FLOAT,
      activepower: DataTypes.FLOAT,
      reactivepower: DataTypes.FLOAT,
      apparentpower: DataTypes.FLOAT,
      idDevice: DataTypes.INTEGER,
    },
    {
      createdAt: false,
      updatedAt: false,
    }
  )
  const User = db.define(
    'user',
    {
      idDser: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
      },
      username: DataTypes.STRING,
      password: DataTypes.STRING,
    },
    {
      createdAt: false,
      updatedAt: false,
    }
  )

  const DeviceEnergyConsumption = db.define('deviceenergyconsumption')

  Device.hasMany(EnergyConsumption, { foreignKey: 'idDevice' })

  EnergyConsumption.belongsToMany(Device, { through: DeviceEnergyConsumption })

  db._tables = {
    Device,
    EnergyConsumption,
    User,
    Area,
    Policies,
  }
}
async function insertRealData() {
  const { Device, EnergyConsumption, User, Area } = db._tables

  //* *INSERT Users */
  const BMW = await User.create({
    username: 'BMW_Munich',
    password: 'BMW',
  })

  const Siemens = await User.create({
    username: 'Siemens_Munich',
    password: 'Siemens',
  })
}

/**
 * Function to initialize the database. This is exported and called in the main api.js file
 */
async function initializeDatabase() {
  // Call the function for the database structure definition
  defineDBStructure()
  // Synchronize Sequelize with the actual database
  await db.sync({ force: false, alter: true })
  // Call the function to insert some fake data
  await insertRealData()
  return db
}

export default initializeDatabase
