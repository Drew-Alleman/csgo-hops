
#include "cheat.h"

LPCWSTR DLL_NAME = L"client.dll";
ptrdiff_t dwForceJump = 0x52B9C0C;
ptrdiff_t dwLocalPlayer = 0xDE8964;
ptrdiff_t m_fFlags = 0x104;

std::set<int> validMoves = { 257 , 512, 262, 263, 261 } ;

class LocalPlayer {

private:
	uintptr_t gameAddress;
	uintptr_t localPlayerAddress;

public:
	bool bhop() {
		int move = moveType();
		if (validMoves.find(move) != validMoves.end()) {
			return jump();
		}
		return false;
	}

	bool jump() {
		*reinterpret_cast<int*>(gameAddress + dwForceJump) = 6;
		return true;
	}

	int moveType() {
		return *reinterpret_cast<int*>(localPlayerAddress + m_fFlags);
	}

	void getClientDLLAddress() {
		gameAddress = (uintptr_t)GetModuleHandle(DLL_NAME);
	}

	void getAddresses() {
		if (gameAddress == NULL)
			getClientDLLAddress();
		if (gameAddress != NULL and localPlayerAddress == NULL)
			updateLocalPlayerAddress();
	}

	void updateLocalPlayerAddress() {
		localPlayerAddress = *reinterpret_cast<uintptr_t*>(gameAddress + dwLocalPlayer);
	}

	bool isValid() {
		return gameAddress != NULL and localPlayerAddress != NULL;
	}
};


void enableBhop() {
	LocalPlayer localPlayer = LocalPlayer();
	while (true)
	{
		if (!localPlayer.isValid()) {
			localPlayer.getAddresses();
			Sleep(100);
			continue;
		}
		if (GetAsyncKeyState(VK_END))
			break;
		else if ((GetAsyncKeyState(VK_SPACE) & 0x8000) and localPlayer.bhop()) {
			continue;
		} 
		Sleep(1);
	}
}