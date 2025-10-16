import { Link } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

export default function Navbar() {
  const { user, logout } = useAuth()

  return (
    <nav className="bg-white border-b">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <Link to="/" className="font-semibold text-primary-700">Eventgrid</Link>
        </div>
        <div className="flex items-center gap-3">
          {!user && (
            <>
              <Link to="/login" className="text-sm">Login</Link>
              <Link to="/register" className="text-sm bg-primary-600 text-white px-3 py-1 rounded">Sign up</Link>
              <Link to="/register-organizer" className="text-sm">Sign up as Organizer</Link>
            </>
          )}
          {user && (
            <>
              <Link to="/dashboard" className="text-sm">Dashboard</Link>
              {/* Role-based quick links */}
              {user.role === 'organizer' && (
                <Link to="/dashboard/my-events" className="text-sm">My Events</Link>
              )}
              {user.role === 'admin' && (
                <>
                  <Link to="/dashboard/my-events" className="text-sm">My Events</Link>
                  <Link to="/dashboard/manage-users" className="text-sm">Manage Users</Link>
                </>
              )}
              {user.role === 'user' && (
                <Link to="/dashboard/my-tickets" className="text-sm">My Tickets</Link>
              )}
              <button onClick={logout} className="text-sm text-red-600">Logout</button>
            </>
          )}
        </div>
      </div>
    </nav>
  )
}
