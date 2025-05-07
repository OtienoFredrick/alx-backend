title: MongoDB Customer Transactions Analysis
description: >
  A MongoDB project analyzing customer transactions and products using queries and aggregation pipelines.

files:
  - customerTransactions.js: JavaScript dataset loader for MongoDB
  - MongoDB.txt: Script containing all executed MongoDB commands and queries

instructions:
  - Ensure MongoDB is installed and running
  - Use `mongo` shell to run the script
  - Load data using: `load("customerTransactions.js")`

counts:
  - Count documents:
      product: db.product.count()
      customer: db.customer.count()
      transactions: db.transactions.count()
      transaction_contains: db.transaction_contains.count()
  - Count total transactions:
      query: >
        db.customer.aggregate([
          { $unwind: "$transaction" },
          { $group: { _id: null, transaction_count: { $sum: 1 } } }
        ])
  - Count total items in all transactions:
      query: >
        db.customer.aggregate([
          { $unwind: "$transaction" },
          { $unwind: "$transaction.transaction_contains" },
          { $group: { _id: null, items_count: { $sum: 1 } } }
        ])

queries:
  - Alcohol UPCs:
      query: db.product.find({ category: "Alcohol" }, { upc: 1, _id: 0 })
  - Customer with transaction ID 104:
      query: db.customer.find({ "transaction.transaction_ID": "104" }, { customer_ID: 1, _id: 0 })
  - Customers with first transaction under $50:
      query: >
        db.customer.aggregate([
          { $project: { customer_ID: 1, first_transaction: { $arrayElemAt: ["$transaction", 0] } } },
          { $match: { "first_transaction.total": { $lt: 50 } } },
          { $count: "low_spending_first_timers" }
        ])
  - Products missing description:
      query: db.product.find({ product_Description: { $exists: false } }, { product_name: 1, _id: 0 })
  - Products by Pepsi or Coca-Cola:
      query: db.product.count({ brand: { $in: ["Pepsi", "Coca-Cola"] } })
  - Products < $10 with quantity ≥ 50:
      query: db.product.find({ marked_price: { $lt: 10 }, quantity: { $gte: 50 } }, { product_name: 1, _id: 0 })
  - Customers with no transactions:
      query: >
        db.customer.count({
          $or: [
            { transaction: { $exists: false } },
            { transaction: { $size: 0 } }
          ]
        })
  - Transactions with alcohol:
      steps:
        - Step 1: >
            var alcoholUpcs = db.product.find({ category: "Alcohol" }).toArray().map(function(p) {
              return p.upc;
            });
        - Step 2: >
            db.customer.aggregate([
              { $unwind: "$transaction" },
              { $unwind: "$transaction.transaction_contains" },
              { $match: { "transaction.transaction_contains.upc": { $in: alcoholUpcs } } },
              { $group: { _id: "$transaction.transaction_ID" } }
            ])

notes:
  - Use `use customerTransactions` before running queries
  - Always use `.toArray()` before `.map()` in shell
  - Save screenshots and results in a PDF as required

author:
  name: Fredrick Otieno
  program: Software Engineering Coursework

