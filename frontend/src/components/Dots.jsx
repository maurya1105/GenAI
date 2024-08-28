import "./Dots.css";
function Dots() {
  
  return (
    <>
      <div className="h-1/4 aspect-square  rounded-full bg-white duration-100 dots"></div>
      <div className="h-1/4 aspect-square  rounded-full bg-white duration-100 dots" style={{animationDelay:"0.25s"}}></div>
      <div className="h-1/4 aspect-square  rounded-full bg-white duration-100 dots" style={{animationDelay:"0.5s"}}></div>
    </>
  );
}
export default Dots;
