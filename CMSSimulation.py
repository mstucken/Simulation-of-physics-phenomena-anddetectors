print "Starting"

import ROOT as rt

def SetParticleParameters(lepton):
	if lepton=="mu-":
		return [106, -1]
	elif lepton=="mu+":
		return [106, 1]
	elif lepton=="e-":
		return [0.5, -1]
	elif lepton=="e+":
		return [0.5, 1]
	else:
		raise ValueError("Not the right input on the funtion SetParticleParameters")

class Particle:
	def __init__(self, pos, fourmomentum, lepton):
		self.Position = pos
		self.FourMomentum = fourmomentum
		self.Lepton = lepton
		self.Mass = (SetParticleParameters("e+"))[0]
		self.Charge = (SetParticleParameters("e+"))[1]
	
	def SetPosition(self, pos):
		self.Position = pos
		
	def SetFourMomentum(self, momentum):
		self.FourMomentum = momentum

def CentralDetectorPositionCheck(detector, Particle):
	if (Particle.Position.Z() == detector.Width and Particle.Position.Perp() <= detector.Height):
		return True
	elif (Particle.Position.Z() == (-1*detector.Width) and Particle.Position.Perp() <= detector.Height):
		return True
	elif (Particle.Position.Perp() == detector.Height and abs(Particle.Position.Z()) <= detector.Width):
		return True
	else:
		raise ValueError("The particle is not in the right position in the detector")
		return False


class CentralDetector:
	def __init__(self, height, width, thickness):
		self.Height = height
		self.Width = width
		self.MaxWidth = width + thickness
		self.MaxHeight = height + thickness
		
	def printheight(self):
		print self.MaxWidth
		return self.MaxWidth


det = CentralDetector(1,1,1)
vec = rt.TLorentzVector(0.5,0.3,1,1)
vec2 = rt.TLorentzVector(0,1,0.3,1)
vec3 = rt.TLorentzVector(0.5,0.3,0.3,1)
par1 = Particle(vec,vec,"mu+")
par2 = Particle(vec2,vec2,"mu+")
par3 = Particle(vec3,vec3,"mu+")
print CentralDetectorPositionCheck(det, par1)
print CentralDetectorPositionCheck(det, par2)
print CentralDetectorPositionCheck(det, par3)


