import {ClerkProvider} from "@clerk/clerk-react"
import {BrowserRouter} from "react-router-dom";

// Import your Publishable Key from clerk (authentication)
const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!PUBLISHABLE_KEY) {
  throw new Error('Missing Publishable Key')
}


// Any of the children that gets wrapped in the function gets wrapped in a browserrouter and clerkProvider
export default function ClerkProviderWithRoutes({children}){

    return (
        <ClerkProvider publishableKey={PUBLISHABLE_KEY}>
        <BrowserRouter>{children}</BrowserRouter>
        </ClerkProvider>
    )
}