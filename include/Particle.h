/* Copyright (C) 2010- Imperial College London and others.
   
   Please see the AUTHORS file in the main source directory for a full
   list of copyright holders.
   
   Dr Gerard J Gorman
   Applied Modelling and Computation Group
   Department of Earth Science and Engineering
   Imperial College London
   
   g.gorman@imperial.ac.uk
   
   This library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License.
   
   This library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.
   
   You should have received a copy of the GNU Lesser General Public
   License along with this library; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
   USA
*/
#include <iostream>
#include <vector>

using namespace std;

#ifndef Particle_H
#define Particle_H
class Particle
{
 public:
  Particle(double coordinates[], int dim, int cell, double local_coords[]);
  ~Particle();
  virtual void view();

 protected:
  int            cell;
  vector<double> position;
  vector<double> local_coords;
};
#endif // Particle_H
