import { useEffect, useState } from 'react'
import { getMyOrders } from '../../services/orders'

export default function UserDashboard() {
  const [orders, setOrders] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let mounted = true
    getMyOrders().then((res) => {
      if (!mounted) return
      setOrders(res.orders || [])
    }).finally(() => mounted && setLoading(false))
    return () => { mounted = false }
  }, [])

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">My Tickets</h2>
      {loading && <div>Loading...</div>}
      {!loading && orders.length === 0 && <div>No orders yet.</div>}
      <ul className="space-y-2">
        {orders.map(o => (
          <li key={o.id} className="border rounded p-3 bg-white">
            <div className="text-sm text-gray-600">Order #{o.id}</div>
            <div className="font-medium">Total ${(o.total_amount||0)/100}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
