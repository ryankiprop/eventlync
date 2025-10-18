# EventLync API Demo Script
# Run these commands to test the EventLync API endpoints

echo "🔍 Testing EventLync API..."
echo "============================="

# 1. Health Check
echo ""
echo "1. Health Check:"
curl -s https://eventlync.onrender.com | jq .

# 2. API Documentation
echo ""
echo "2. API Documentation:"
curl -s https://eventlync.onrender.com/api/docs/swagger.json | jq '.info'

# 3. Test M-Pesa Environment Variables
echo ""
echo "3. M-Pesa Configuration:"
curl -s https://eventlync.onrender.com/api/payments/mpesa/test-env | jq .

# 4. Get Public Events
echo ""
echo "4. Public Events:"
curl -s "https://eventlync.onrender.com/api/events?page=1&per_page=5" | jq '.items[0]'

echo ""
echo "🎯 API Testing Complete!"
echo "📖 Full API docs: https://eventlync.onrender.com/api/docs/swagger.json"
echo "🌐 Frontend: https://eventlync.vercel.app"
