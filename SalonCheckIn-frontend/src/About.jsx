import React from "react";

const About = () => {
  return (
    <>
      <div className="container-fluid about">
        <h1 className="text-center text-capitalize" id="about">
          about us
        </h1>
        <hr className="w-50 mx-auto pt-4" />
        <div className="row mb-5">
          <div className="col-lg-6 col-md-6">
            <img
              src="/images/instruments.png"
              className="img-fluid"
              alt="img"
            />
          </div>
          <div className="col-lg-6 col-md-6 ">
            <h3 className="text-capitalize" id="content">
              what do we do?
            </h3>
            <p>
              {" "}
              Lorem ipsum, dolor sit amet consectetur adipisicing elit. Autem
              corporis fuga cum enim, explicabo quam ipsum! Tenetur quos maxime
              repellat ipsam harum quaerat impedit error! Voluptas non fugiat
              quisquam, nihil inventore est. Similique, praesentium doloribus?
              Quos quae modi delectus atque aut, numquam distinctio et, est
              deleniti, minus eos magni maxime? Lorem ipsum, dolor sit amet
              consectetur adipisicing elit. Autem corporis fuga cum enim,
              explicabo quam ipsum! Tenetur quos maxime repellat ipsam harum
              quaerat impedit error! Voluptas non fugiat quisquam, nihil
              inventore est. Similique, praesentium doloribus? Quos quae modi
              delectus atque aut, numquam distinctio et, est deleniti, minus eos
              magni maxime? Lorem ipsum, dolor sit amet consectetur adipisicing
              elit. Autem corporis fuga cum enim, explicabo quam ipsum! Tenetur
              quos maxime repellat ipsam harum quaerat impedit error! Voluptas
              non fugiat quisquam, nihil inventore est. Similique, praesentium
              doloribus? Quos quae modi delectus atque aut, numquam distinctio
              et, est deleniti, minus eos magni maxime?
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
