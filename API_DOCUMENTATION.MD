# Optryn API Documentation

## Inventory Endpoints

### 1. Stock Entry
- **Endpoint:** POST `/inventory/entrada`
- **Description:** Increases the available stock of a product.
- **Body** (JSON):
```json
{
  "productID": 1,
  "quantity": 100
}
Response (JSON):

json
Copiar código
{
  "message": "Stock increased successfully",
  "movement": {
    "id": 1,
    "product_id": 1,
    "type": "entrada",
    "quantity": 100,
    "stock_before": 200,
    "stock_after": 300,
    "date": "2025-12-12T23:24:54.025508"
  }
}
2. Stock Exit (Sales)
Endpoint: POST /inventory/salida

Description: Registers a sale and decreases the available stock.

Body (JSON):

json
Copiar código
{
  "productID": 1,
  "quantity": 5
}
Response (JSON):

json
Copiar código
{
  "message": "Sale registered successfully",
  "movement": {
    "id": 2,
    "product_id": 1,
    "type": "salida",
    "quantity": 5,
    "stock_before": 300,
    "stock_after": 295,
    "date": "2025-12-12T23:30:10.123456"
  }
}
3. Stock Adjustment
Endpoint: POST /inventory/ajuste

Description: Adjusts the stock of a product to a specific value.

Body (JSON):

json
Copiar código
{
  "productID": 1,
  "new_stock": 500
}
Response (JSON):

json
Copiar código
{
  "message": "Stock adjusted successfully",
  "movement": {
    "id": 3,
    "product_id": 1,
    "type": "ajuste",
    "quantity": 500,
    "stock_before": 295,
    "stock_after": 500,
    "date": "2025-12-12T23:35:00.654321"
  }
}
4. Inventory Movements (optional filter)
Endpoint: GET /inventory/movimientos

Optional query params:

movement_type → "entrada", "salida" or "ajuste"

start_date → ISO datetime

end_date → ISO datetime

Description: Returns the list of movements filtered by the parameters.

Response (JSON):

json
Copiar código
[
  {
    "id": 1,
    "product_id": 1,
    "type": "entrada",
    "quantity": 100,
    "stock_before": 200,
    "stock_after": 300,
    "date": "2025-12-12T23:24:54.025508"
  },
  {
    "id": 2,
    "product_id": 1,
    "type": "salida",
    "quantity": 5,
    "stock_before": 300,
    "stock_after": 295,
    "date": "2025-12-12T23:30:10.123456"
  }
]