import { useEffect, useState } from 'react'
import { getEventTickets, createTicketType, updateTicketType, deleteTicketType } from '../../services/tickets'

export default function TicketManager({ eventId }) {
  const [tickets, setTickets] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [form, setForm] = useState({ name: '', price: '', quantity_total: '' })
  const [submitting, setSubmitting] = useState(false)
  const [status, setStatus] = useState(null)
  const [editingId, setEditingId] = useState(null)
  const [editForm, setEditForm] = useState({ name: '', price: '', quantity_total: '' })

  const load = () => {
    setLoading(true)
    getEventTickets(eventId)
      .then((res) => { setTickets(res.tickets || []); setError(null) })
      .catch((e) => setError(e?.response?.data?.message || 'Failed to load ticket types'))
      .finally(() => setLoading(false))
  }

  useEffect(() => { load() }, [eventId])

  const onSubmit = async (e) => {
    e.preventDefault()
    setSubmitting(true)
    setStatus(null)
    try {
      const payload = {
        name: form.name.trim(),
        price: Math.round(parseFloat(form.price) * 100) || 0,
        quantity_total: parseInt(form.quantity_total || '0', 10)
      }
      if (!payload.name || payload.price <= 0 || payload.quantity_total <= 0) {
        setStatus({ err: 'Provide valid name, price (>0), and quantity (>0).' })
      } else {
        await createTicketType(eventId, payload)
        setForm({ name: '', price: '', quantity_total: '' })
        setStatus({ ok: 'Ticket type created' })
        load()
      }
    } catch (e) {
      setStatus({ err: e?.response?.data?.message || 'Failed to create ticket type' })
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="mt-8">
      <h3 className="text-lg font-semibold mb-2">Manage Ticket Types</h3>
      <form onSubmit={onSubmit} className="grid grid-cols-1 md:grid-cols-4 gap-3 p-3 bg-gray-50 border rounded">
        <input className="border rounded px-3 py-2" placeholder="Name" value={form.name} onChange={e => setForm(f => ({ ...f, name: e.target.value }))} />
        <input className="border rounded px-3 py-2" placeholder="Price (USD)" value={form.price} onChange={e => setForm(f => ({ ...f, price: e.target.value }))} />
        <input className="border rounded px-3 py-2" placeholder="Quantity" value={form.quantity_total} onChange={e => setForm(f => ({ ...f, quantity_total: e.target.value }))} />
        <button type="submit" disabled={submitting} className="bg-primary-600 text-white px-4 py-2 rounded">{submitting ? 'Adding...' : 'Add Ticket'}</button>
      </form>
      {status?.err && <div className="text-red-600 mt-2">{status.err}</div>}
      {status?.ok && <div className="text-green-700 mt-2">{status.ok}</div>}

      <div className="mt-4">
        {loading && <div>Loading ticket types...</div>}
        {error && <div className="text-red-600">{error}</div>}
        {!loading && !error && (
          <ul className="space-y-2">
            {tickets.map(t => (
              <li key={t.id} className="flex items-center justify-between border rounded p-3 bg-white">
                <div className="flex-1 pr-4">
                  {editingId === t.id ? (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                      <input className="border rounded px-3 py-2" value={editForm.name} onChange={e => setEditForm(f => ({ ...f, name: e.target.value }))} />
                      <input className="border rounded px-3 py-2" value={editForm.price} onChange={e => setEditForm(f => ({ ...f, price: e.target.value }))} />
                      <input className="border rounded px-3 py-2" value={editForm.quantity_total} onChange={e => setEditForm(f => ({ ...f, quantity_total: e.target.value }))} />
                    </div>
                  ) : (
                    <>
                      <div className="font-medium">{t.name}</div>
                      <div className="text-sm text-gray-600">${(t.price||0)/100} • {t.quantity_total - (t.quantity_sold||0)} left</div>
                    </>
                  )}
                </div>
                <div className="flex items-center gap-2">
                  {editingId === t.id ? (
                    <>
                      <button
                        className="px-3 py-1 border rounded"
                        onClick={async () => {
                          const payload = {
                            name: editForm.name.trim(),
                            price: Math.round(parseFloat(editForm.price) * 100) || 0,
                            quantity_total: parseInt(editForm.quantity_total || '0', 10)
                          }
                          if (!payload.name || payload.price <= 0 || payload.quantity_total <= 0) {
                            setStatus({ err: 'Provide valid name, price (>0), and quantity (>0).' })
                            return
                          }
                          await updateTicketType(eventId, t.id, payload)
                          setEditingId(null)
                          setEditForm({ name: '', price: '', quantity_total: '' })
                          load()
                        }}
                      >Save</button>
                      <button className="px-3 py-1 border rounded" onClick={() => { setEditingId(null); setEditForm({ name: '', price: '', quantity_total: '' }) }}>Cancel</button>
                    </>
                  ) : (
                    <>
                      <button
                        className="px-3 py-1 border rounded"
                        onClick={() => {
                          setEditingId(t.id)
                          setEditForm({ name: t.name, price: (t.price||0)/100, quantity_total: t.quantity_total })
                        }}
                      >Edit</button>
                      <button
                        className="px-3 py-1 border rounded text-red-600"
                        onClick={async () => { await deleteTicketType(eventId, t.id); load() }}
                      >Delete</button>
                    </>
                  )}
                </div>
              </li>
            ))}
            {tickets.length === 0 && <li className="text-gray-600">No ticket types yet.</li>}
          </ul>
        )}
      </div>
    </div>
  )
}
