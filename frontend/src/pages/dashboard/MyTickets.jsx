import { useEffect, useState } from 'react'
import { getMyOrders } from '../../services/orders'

export default function MyTickets() {
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
    <div className="max-w-6xl mx-auto p-4">
      <h1 className="text-2xl font-semibold mb-4">My Tickets</h1>
      {loading && <div>Loading...</div>}
      {!loading && orders.length === 0 && <div>No orders yet.</div>}
      <ul className="space-y-3">
        {orders.map(o => (
          <li key={o.id} className="border rounded p-3 bg-white">
            <div className="text-sm text-gray-600">Order #{o.id}</div>
            <div className="font-medium">Total ${(o.total_amount||0)/100}</div>
            <div className="text-xs text-gray-500">Items: {o.items?.length || 0}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}
