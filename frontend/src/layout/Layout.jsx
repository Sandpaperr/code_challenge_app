import "react"
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react"
import { Outlet, Link, Navigate } from "react-router-dom"

// Build the layout that shows everywhere in the website
export function Layout(){
    return <div className="app-layout">
        <header className="app-header">
            <div className="header-content">
                <h1>Code Challenge Generator</h1>
                <nav>
                    <SignedIn>
                        <Link to="/"> Generate Challenge</Link>
                        <Link to="/history"> History</Link>
                        <UserButton/>
                    </SignedIn>
                </nav>

            </div>

        </header>

        <main className="app-main">
            <SignedOut>
                <Navigate to="/sign-in" replace/>
            </SignedOut>

            <SignedIn>
                {/*Outlet is a holder for whatever is passedd inside layout from the app.jsx*/}
                <Outlet/>
            </SignedIn>

        </main>
        
    </div>
}