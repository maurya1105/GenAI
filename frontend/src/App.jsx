import Home from "./components/Home";
import { nord } from "./Constants";
function App() {
  return (
    <>
      <div
        className="w-full  h-screen overflow-hidden  "
        style={{ backgroundColor: nord.dark.a }}
      >
        <Home />
      </div>
    </>
  );
}

export default App;
