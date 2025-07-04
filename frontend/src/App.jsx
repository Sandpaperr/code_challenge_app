import { useState } from 'react'
import ClerkProviderWithRoutes from "./auth/ClerkProviderWithRoutes.jsx"
import { Routes, Route } from 'react-router-dom'
import { Layout } from './layout/Layout.jsx'
import { ChallengeGenerator } from './challenge/ChallengeGenerator.jsx'
import { HistoryPannel } from './history/HistoryPannel.jsx'
import { AuthenticationPage } from './auth/AuthanticationPage.jsx'
import './App.css'

function App() {
    return <ClerkProviderWithRoutes>
        <Routes>
            <Route path="/sign-in/*" element={<AuthenticationPage/>}/>
            <Route path="/sign-up" element={<AuthenticationPage/>}/>

            {/* everything will be rendered inside the Layout component */}
            <Route element={<Layout/>}>
                <Route path="/" element={<ChallengeGenerator/>}/>
                <Route path="/history" element={<HistoryPannel/>}/>
            </Route>
        </Routes>
    </ClerkProviderWithRoutes>
}

export default App
